"""Generate the animated sky banner used by the GitHub profile.

The GIF is deliberately self-contained: GitHub can display it as an image without
requiring JavaScript, hover state, or interactive SVG embedding.
"""
from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
ASSET_DIR = ROOT / "assets" / "profile"
SOURCE = ASSET_DIR / "cat-mascot-clean.png"
OUTPUT_GIF = ASSET_DIR / "sky-cat.gif"
OUTPUT_STILL = ASSET_DIR / "sky-cat-still.png"

WIDTH, HEIGHT = 1200, 1100
FRAME_COUNT = 32


def remove_checkerboard(image: Image.Image) -> Image.Image:
    """Remove the neutral light checkerboard from the generated mascot fallback."""
    image = image.convert("RGBA")
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            neutral = max(r, g, b) - min(r, g, b) <= 8
            if neutral and min(r, g, b) >= 205:
                pixels[x, y] = (r, g, b, 0)
    bbox = image.getchannel("A").getbbox()
    if bbox:
        image = image.crop(bbox)
    return image


def make_cat() -> Image.Image:
    mascot = remove_checkerboard(Image.open(SOURCE))
    mascot.thumbnail((230, 230), Image.Resampling.LANCZOS)
    return mascot


def gradient_background() -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT))
    pixels = image.load()
    top = (5, 10, 30)
    bottom = (26, 17, 58)
    for y in range(HEIGHT):
        ratio = y / max(1, HEIGHT - 1)
        for x in range(WIDTH):
            shimmer = int(3 * math.sin((x / WIDTH) * math.pi * 2))
            pixels[x, y] = tuple(max(0, min(255, int(top[i] * (1 - ratio) + bottom[i] * ratio) + shimmer)) for i in range(3))
    return image


def draw_cloud(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float, alpha: int = 170) -> None:
    fill = (174, 183, 226, alpha)
    cloud = Image.new("RGBA", (260, 120), (0, 0, 0, 0))
    cloud_draw = ImageDraw.Draw(cloud)
    cloud_draw.ellipse((12, 45, 120, 108), fill=fill)
    cloud_draw.ellipse((70, 18, 180, 108), fill=fill)
    cloud_draw.ellipse((140, 42, 248, 108), fill=fill)
    cloud_draw.rounded_rectangle((34, 58, 222, 108), radius=26, fill=fill)
    cloud = cloud.resize((int(cloud.width * scale), int(cloud.height * scale)), Image.Resampling.LANCZOS)
    draw._image.alpha_composite(cloud, (x, y))


def draw_frame(index: int, cat: Image.Image) -> Image.Image:
    frame = gradient_background().convert("RGBA")
    draw = ImageDraw.Draw(frame, "RGBA")

    # Moon halo and soft midnight atmospheric bands.
    for radius, alpha in [(150, 10), (118, 15), (88, 24)]:
        draw.ellipse((930 - radius, 120 - radius, 930 + radius, 120 + radius), fill=(157, 145, 255, alpha))
    draw.ellipse((900, 90, 960, 150), fill=(231, 233, 255, 245))
    draw.ellipse((919, 100, 979, 160), fill=(26, 24, 63, 240))

    # Parallax clouds: distant clouds drift slowly; the foreground cloud crosses
    # the cat's route, making the loop feel like a tiny world rather than a sticker.
    draw_cloud(draw, 80 - (index * 3) % 1450, 220, 0.75, 112)
    draw_cloud(draw, 640 - (index * 6) % 1550, 360, 0.52, 145)
    draw_cloud(draw, 300 - (index * 10) % 1500, 610, 1.15, 165)
    draw_cloud(draw, 870 - (index * 8) % 1500, 760, 0.68, 125)

    random.seed(41)
    for _ in range(52):
        x = random.randint(0, WIDTH - 1)
        y = random.randint(18, 720)
        r = random.choice([1, 1, 1, 2])
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(232, 235, 255, random.randint(110, 240)))
    # Constellation threads and an occasional shooting star.
    constellation = [(160, 240), (222, 188), (284, 230), (340, 168), (405, 218)]
    draw.line(constellation, fill=(173, 175, 255, 120), width=1)
    for x, y in constellation:
        draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill=(217, 215, 255, 230))
    streak_x = (index * 38) % 1320 - 120
    streak_y = 420 - (index * 5) % 220
    draw.line((streak_x, streak_y, streak_x + 80, streak_y - 28), fill=(255, 225, 244, 190), width=2)
    # Distant mountain silhouettes.
    mountain = [(0, 930), (115, 820), (220, 910), (342, 790), (480, 918), (610, 816), (755, 920), (885, 800), (1030, 910), (1130, 838), (1200, 916), (1200, 1100), (0, 1100)]
    draw.polygon(mountain, fill=(30, 33, 78, 235))
    draw.polygon([(0, 1000), (170, 898), (330, 986), (520, 880), (700, 990), (920, 886), (1200, 994), (1200, 1100), (0, 1100)], fill=(12, 16, 43, 250))


    # Cat sweeps diagonally through the entire tall canvas, looping back like a
    # tiny navigator crossing the profile rather than a mascot stuck in a header.
    progress = (index / (FRAME_COUNT - 1))
    x = int(90 + 760 * (0.5 + 0.5 * math.sin(progress * math.pi * 2)))
    y = int(155 + 700 * progress + 18 * math.sin(progress * math.pi * 6))
    bobbed = cat.rotate(3 * math.sin(progress * math.pi * 4), resample=Image.Resampling.BICUBIC, expand=True)
    frame.alpha_composite(bobbed, (x, y))

    # A tiny motion trail and status labels keep the scene tied to AYU.OS.
    draw = ImageDraw.Draw(frame, "RGBA")
    draw.line((40, 42, 275, 42), fill=(194, 188, 255, 180), width=2)
    draw.text((40, 56), "AYU.OS / FULL PROFILE NIGHT ROUTE", fill=(235, 233, 255, 230))
    draw.text((40, 78), "Nova // roaming across the canvas", fill=(188, 198, 255, 230))
    draw.text((40, 1030), "NOVA ROUTE COMPLETE · RETURNING TO ORBIT", fill=(206, 208, 255, 220))
    draw.text((1010, 1030), "MOON 01 · ALT 420", fill=(206, 208, 255, 220))
    return frame.convert("RGB")


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Mascot source missing: {SOURCE}")
    cat = make_cat()
    frames = [draw_frame(index, cat) for index in range(FRAME_COUNT)]
    frames[0].save(OUTPUT_GIF, save_all=True, append_images=frames[1:], duration=105, loop=0, optimize=True, disposal=2)
    frames[FRAME_COUNT // 2].save(OUTPUT_STILL, format="PNG", optimize=True)
    print(f"Generated {OUTPUT_GIF}")
    print(f"Generated {OUTPUT_STILL}")


if __name__ == "__main__":
    main()
