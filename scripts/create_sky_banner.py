"""Generate the animated sky banner used by the GitHub profile.

The GIF is deliberately self-contained: GitHub can display it as an image without
requiring JavaScript, hover state, or interactive SVG embedding.
"""
from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSET_DIR = ROOT / "assets" / "profile"
SOURCE = ASSET_DIR / "cat-mascot-clean.png"
OUTPUT_GIF = ASSET_DIR / "sky-cat.gif"
OUTPUT_STILL = ASSET_DIR / "sky-cat-still.png"

WIDTH, HEIGHT = 1200, 1800
FRAME_COUNT = 120


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


PIXEL = 2
PIXEL_PALETTE = {
    "outline": (13, 17, 23, 255),
    "fur": (240, 198, 98, 255),
    "fur_light": (255, 231, 150, 255),
    "fur_shadow": (139, 96, 30, 255),
    "cream": (240, 246, 252, 255),
    "pink": (255, 126, 146, 255),
    "blue": (88, 166, 255, 255),
    "green": (63, 185, 80, 255),
}


def pixel_cat(state: str, phase: int = 0) -> Image.Image:
    """Draw Nova as a crisp 32px pixel-art character with state-specific poses."""
    canvas = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    d = ImageDraw.Draw(canvas, "RGBA")
    c = PIXEL_PALETTE
    def r(x0, y0, x1, y1, color):
        d.rectangle((x0, y0, x1, y1), fill=color)
    def p(x, y, color):
        r(x, y, x, y, color)

    # Ground shadow and tiny status pixel give the sprite a relationship with the floor.
    if state not in {"sleep", "acro_sleep"}:
        r(6, 27, 25, 29, (1, 4, 7, 115))
        p(26, 27, c["green"])

    if state == "sleep":
        # Curled crescent: face tucked into tail, paws folded, eyes closed.
        r(7, 15, 24, 25, c["fur_shadow"])
        r(9, 12, 23, 23, c["fur"])
        r(12, 14, 22, 22, c["cream"])
        r(9, 9, 20, 17, c["fur"])
        r(10, 7, 13, 10, c["fur"]); r(17, 7, 20, 10, c["fur"])
        r(11, 9, 18, 14, c["cream"])
        r(13, 12, 14, 12, c["outline"]); r(17, 12, 18, 12, c["outline"])
        r(14, 14, 17, 14, c["pink"])
        for i in range(phase % 3):
            p(25 + i, 8 - i * 3, c["blue"])
        r(5, 21, 9, 24, c["fur"]); r(3, 23, 8, 25, c["fur"])
    elif state == "acro_sleep":
        # Upside-down acrobatic nap: paws in the air and tail forming a loop.
        r(8, 15, 23, 23, c["fur_shadow"])
        r(10, 12, 22, 21, c["fur"])
        r(12, 14, 20, 20, c["cream"])
        r(10, 20, 13, 25, c["fur_light"]); r(19, 20, 22, 25, c["fur_light"])
        r(12, 8, 20, 15, c["fur"])
        r(11, 6, 14, 10, c["fur"]); r(18, 6, 21, 10, c["fur"])
        r(13, 9, 19, 13, c["cream"])
        r(14, 11, 15, 11, c["outline"]); r(17, 11, 18, 11, c["outline"])
        r(15, 13, 17, 13, c["pink"])
        r(4, 10, 8, 13, c["fur"]); r(2, 8, 6, 10, c["fur"]); r(2, 6, 3, 8, c["fur_light"])
        r(23, 8, 27, 11, c["fur"]); r(26, 10, 29, 13, c["fur"])
        p(27, 6, c["blue"]); p(28, 4, c["blue"])
    else:
        # Upright base pose with expressive, state-driven limbs.
        walking = state == "walk"
        licking = state == "lick"
        greeting = state in {"greet", "wake"}
        r(9, 15, 22, 25, c["fur_shadow"])
        r(10, 13, 22, 23, c["fur"])
        r(12, 15, 20, 21, c["cream"])
        r(7, 7, 21, 17, c["fur"])
        r(9, 5, 13, 9, c["fur"]); r(17, 5, 21, 9, c["fur"])
        r(10, 8, 19, 14, c["cream"])
        p(12, 10, c["outline"]); p(17, 10, c["outline"])
        r(14, 12, 16, 12, c["pink"])
        r(15, 13, 16, 14, c["pink"] if licking else c["outline"])
        # Tail waves differently while walking, resting, or waking.
        tail_y = 18 + int(2 * math.sin(phase * 0.9)) if walking else 20
        r(4, tail_y, 9, tail_y + 3, c["fur"]); r(2, tail_y - 2, 5, tail_y + 1, c["fur"])
        p(1, tail_y - 3, c["fur_light"])
        if licking:
            r(20, 15, 23, 19, c["fur_light"]); r(21, 13, 22, 16, c["fur"])
            r(16, 14, 17, 16, c["pink"])
        elif greeting:
            r(20, 11, 23, 16, c["fur_light"]); r(22, 9, 24, 12, c["fur"]); p(24, 8, c["cream"])
        else:
            leg_a = 24 + (phase % 2)
            leg_b = 24 + ((phase + 1) % 2)
            r(11, leg_a, 14, 28, c["cream"]); r(18, leg_b, 21, 28, c["cream"])
            r(10, 28, 14, 29, c["outline"]); r(18, 28, 22, 29, c["outline"])
        if state == "wake":
            p(23, 4, c["blue"]); p(25, 3, c["blue"])
    return canvas.resize((32 * PIXEL, 32 * PIXEL), Image.Resampling.NEAREST)


def make_cat() -> Image.Image:
    return pixel_cat("walk", 0)


def profile_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def draw_panel(draw: ImageDraw.ImageDraw, x: int, y: int, width: int, height: int, title: str, lines: list[str], accent=(88, 166, 255, 230)) -> None:
    draw.rounded_rectangle((x, y, x + width, y + height), radius=22, fill=(31, 35, 40, 226), outline=(88, 96, 105, 180), width=2)
    draw.line((x + 22, y + 22, x + 170, y + 22), fill=accent, width=3)
    draw.text((x + 22, y + 38), title.upper(), font=profile_font(22, True), fill=(240, 246, 252, 245))
    cursor = y + 78
    for line in lines:
        draw.text((x + 22, cursor), line, font=profile_font(16), fill=(139, 148, 158, 235))
        cursor += 28


def draw_artifact(draw: ImageDraw.ImageDraw, x: int, y: int, width: int, height: int, number: str, title: str, subtitle: str, accent: tuple[int, int, int, int], index: int, tilt: float = 0.0) -> None:
    """Frame a project like an exhibition artifact instead of a dashboard card."""
    shadow = (x + 12, y + 14, x + width + 12, y + height + 14)
    draw.rounded_rectangle(shadow, radius=8, fill=(1, 4, 7, 150))
    draw.rounded_rectangle((x, y, x + width, y + height), radius=8, fill=(31, 35, 40, 245), outline=(88, 96, 105, 190), width=2)
    inset = 18
    draw.rectangle((x + inset, y + inset, x + width - inset, y + height - 74), fill=(13, 17, 23, 245), outline=(88, 96, 105, 100), width=1)
    # The artifact image is an abstract interface specimen built from deterministic geometry.
    for row in range(3):
        yy = y + inset + 24 + row * 26
        draw.line((x + inset + 18, yy, x + width - inset - 18, yy), fill=(*accent[:3], 48 + row * 18), width=2)
    scan = y + inset + 45 + int((index * 11) % max(20, height - 130))
    draw.line((x + inset + 12, scan, x + width - inset - 12, scan), fill=accent, width=2)
    for dot in range(4):
        px = x + inset + 24 + dot * 42
        py = y + inset + 92 + int(10 * math.sin(index * 0.2 + dot))
        draw.ellipse((px - 4, py - 4, px + 4, py + 4), fill=(*accent[:3], 180))
    draw.text((x + 18, y + height - 59), number, font=profile_font(13, True), fill=accent)
    draw.text((x + 60, y + height - 60), title.upper(), font=profile_font(17, True), fill=(240, 246, 252, 245))
    draw.text((x + 60, y + height - 36), subtitle, font=profile_font(13), fill=(139, 148, 158, 235))


def draw_profile_copy(draw: ImageDraw.ImageDraw, index: int) -> None:
    """Compose the profile as a curated exhibition wall with real project labels."""
    draw.text((52, 178), "AYU.OS / INTERFACE EXHIBITION", font=profile_font(25, True), fill=(240, 246, 252, 245))
    draw.text((52, 216), "A small collection of things I built, researched, and cared enough to finish.", font=profile_font(16), fill=(139, 148, 158, 235))
    draw.line((52, 250, 1148, 250), fill=(88, 96, 105, 150), width=1)
    draw.text((52, 276), "ROOM 01  /  SELECTED ARTIFACTS", font=profile_font(13, True), fill=(88, 166, 255, 220))
    draw_artifact(draw, 52, 310, 510, 270, "01", "AYU.OS", "profile systems · design tokens · CI", (88, 166, 255, 235), index)
    draw_artifact(draw, 638, 310, 510, 270, "02", "AGENTTIP", "x402 · USDC · human + agent payments", (210, 153, 34, 235), index + 7)
    draw_artifact(draw, 52, 640, 510, 270, "03", "LOCAL AI", "Ollama · Docker · Playwright", (63, 185, 80, 235), index + 13)
    draw_artifact(draw, 638, 640, 510, 270, "04", "CLEARVIEW", "calm information systems · product UX", (130, 80, 223, 235), index + 19)
    draw.text((52, 975), "ROOM 02  /  THE PRACTICE", font=profile_font(13, True), fill=(63, 185, 80, 220))
    draw.text((52, 1015), "Systems with a human edge", font=profile_font(25, True), fill=(240, 246, 252, 245))
    draw.text((52, 1052), "local intelligence · interfaces · security · open protocols · community", font=profile_font(15), fill=(139, 148, 158, 235))
    draw.line((52, 1090, 1148, 1090), fill=(88, 96, 105, 140), width=1)
    practice = [
        ("01", "BUILD", "from idea to shipped product", (88, 166, 255, 220)),
        ("02", "RESEARCH", "make complex protocols legible", (210, 153, 34, 220)),
        ("03", "CONNECT", "systems are also people", (63, 185, 80, 220)),
    ]
    for row, (num, title, subtitle, color) in enumerate(practice):
        yy = 1130 + row * 76
        draw.text((60, yy), num, font=profile_font(14, True), fill=color)
        draw.text((110, yy), title, font=profile_font(18, True), fill=(240, 246, 252, 245))
        draw.text((280, yy), subtitle, font=profile_font(15), fill=(139, 148, 158, 235))
        draw.line((110, yy + 32, 1148, yy + 32), fill=(88, 96, 105, 90), width=1)
    draw.text((52, 1390), "ROOM 03  /  OPEN ARCHIVE", font=profile_font(13, True), fill=(130, 80, 223, 220))
    draw.text((52, 1430), "Ajaia Docs · Facial KeyGen · AirGesture · portfolio · field notes.", font=profile_font(17), fill=(240, 246, 252, 240))
    draw.text((52, 1470), "GitHub · ayushetty.me · LinkedIn · X · email", font=profile_font(15), fill=(139, 148, 158, 235))
    draw.line((52, 1510, 1148, 1510), fill=(88, 96, 105, 140), width=1)


def gradient_background() -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT))
    pixels = image.load()
    top = (13, 17, 23)
    bottom = (31, 35, 40)
    for y in range(HEIGHT):
        ratio = y / max(1, HEIGHT - 1)
        for x in range(WIDTH):
            shimmer = int(3 * math.sin((x / WIDTH) * math.pi * 2))
            pixels[x, y] = tuple(max(0, min(255, int(top[i] * (1 - ratio) + bottom[i] * ratio) + shimmer)) for i in range(3))
    return image


def draw_nebula(frame: Image.Image, index: int, layer: int) -> None:
    """Paint layered volumetric nebula ribbons with shifting highlights and dust pockets."""
    haze = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    haze_draw = ImageDraw.Draw(haze, "RGBA")
    centers = [(250, 560), (920, 1040), (340, 1430)]
    cx, cy = centers[layer % len(centers)]
    drift = int(32 * math.sin(index / FRAME_COUNT * math.pi * 2 + layer * 0.8))
    palette = [(44, 66, 92), (72, 54, 110), (38, 83, 86)]
    color = palette[layer % len(palette)]
    for radius, alpha in [(360, 5), (290, 8), (225, 12), (160, 17), (105, 22)]:
        wobble = int(18 * math.sin(index * 0.08 + radius))
        haze_draw.ellipse((cx + drift - radius, cy + wobble - radius // 2, cx + drift + radius, cy + wobble + radius // 2), fill=(*color, alpha))
    for dust in range(14):
        px = cx + drift + int(math.sin(dust * 2.1 + index * 0.04) * (100 + dust * 11))
        py = cy + int(math.cos(dust * 1.7 + index * 0.03) * (70 + dust * 8))
        haze_draw.ellipse((px - 3, py - 3, px + 3, py + 3), fill=(139, 148, 158, 35))
    haze = haze.filter(ImageFilter.GaussianBlur(42 if layer == 0 else 30))
    frame.alpha_composite(haze)


def draw_deep_stars(draw: ImageDraw.ImageDraw, index: int) -> None:
    """Use parallax star fields plus tiny dust grains and occasional star flares."""
    for layer, count in [(0, 150), (1, 78), (2, 34)]:
        random.seed(100 + layer)
        drift = int((index * (layer + 1) * 2.3) % WIDTH)
        for star in range(count):
            x = (random.randint(0, WIDTH - 1) + drift) % WIDTH
            y = random.randint(20, 1500)
            r = random.choice([1, 1, 1, 1, 2]) if layer < 2 else random.choice([1, 2, 2, 3])
            twinkle = int(85 + 150 * (0.5 + 0.5 * math.sin(index * (0.25 + layer * 0.12) + x * 0.07)))
            tint = random.choice([(201, 209, 217), (139, 148, 158), (88, 166, 255), (240, 198, 98)])
            draw.ellipse((x - r, y - r, x + r, y + r), fill=(*tint, twinkle))
            if layer == 2 and star % 9 == 0:
                draw.line((x - r * 4, y, x + r * 4, y), fill=(*tint, max(30, twinkle // 3)), width=1)
                draw.line((x, y - r * 4, x, y + r * 4), fill=(*tint, max(30, twinkle // 3)), width=1)


def draw_solar_system(draw: ImageDraw.ImageDraw, index: int) -> None:
    """Render a dimensional miniature system with glow, shaded worlds, bands, and orbit depth."""
    cx, cy = 815, 285
    for radius in (68, 108, 148):
        draw.ellipse((cx - radius, cy - int(radius * 0.58), cx + radius, cy + int(radius * 0.58)), outline=(88, 96, 105, 70), width=2)
        draw.arc((cx - radius, cy - int(radius * 0.58), cx + radius, cy + int(radius * 0.58)), 192, 350, fill=(139, 148, 158, 75), width=2)
    for glow_r, glow_a in [(65, 8), (53, 12), (43, 18)]:
        draw.ellipse((cx - glow_r, cy - glow_r, cx + glow_r, cy + glow_r), fill=(210, 153, 34, glow_a))
    draw.ellipse((cx - 31, cy - 31, cx + 31, cy + 31), fill=(139, 96, 30, 245), outline=(240, 198, 98, 230), width=3)
    draw.ellipse((cx - 22, cy - 25, cx + 16, cy + 13), fill=(240, 198, 98, 220))
    draw.ellipse((cx - 8, cy - 16, cx + 16, cy - 3), fill=(255, 231, 150, 150))
    planets = [(68, 8, (88, 166, 255), 1.0), (108, 11, (130, 80, 223), -0.7), (148, 15, (63, 185, 80), 0.45)]
    for radius, size, color, speed in planets:
        angle = index / FRAME_COUNT * math.pi * 2 * speed + radius / 90
        px = int(cx + math.cos(angle) * radius)
        py = int(cy + math.sin(angle) * radius * 0.58)
        for glow in (size + 8, size + 4):
            draw.ellipse((px - glow, py - glow, px + glow, py + glow), fill=(*color, 15 if glow > size + 4 else 28))
        draw.ellipse((px - size, py - size, px + size, py + size), fill=(*color, 240), outline=(240, 246, 252, 125), width=1)
        draw.ellipse((px - size // 2, py - size + 2, px + size // 2, py - 1), fill=(240, 246, 252, 55))
        draw.arc((px - size, py - size, px + size, py + size), 200, 330, fill=(1, 4, 7, 125), width=2)
        if radius == 108:
            draw.ellipse((px - size - 12, py - 4, px + size + 12, py + 4), outline=(210, 153, 34, 180), width=2)
            draw.line((px - size - 8, py, px + size + 8, py), fill=(240, 198, 98, 120), width=1)
    draw.text((690, 475), "AYU.OS / ORBITAL INDEX", font=profile_font(15, True), fill=(139, 148, 158, 220))


def draw_motion_guide(draw: ImageDraw.ImageDraw, index: int) -> None:
    """Sparse observatory rails guide the eye without turning the canvas into a dashboard."""
    points = [(40, 155), (590, 420), (40, 480), (1160, 820), (40, 800), (1160, 1145), (40, 1200), (1160, 1510)]
    draw.line(points, fill=(88, 96, 105, 34), width=2)
    pulse = points[(index // 8) % len(points)]
    glow = 4 + int(3 * (0.5 + 0.5 * math.sin(index * 0.42)))
    draw.ellipse((pulse[0] - glow, pulse[1] - glow, pulse[0] + glow, pulse[1] + glow), fill=(88, 166, 255, 150))


def draw_vignette(frame: Image.Image) -> None:
    vignette = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    px = vignette.load()
    cx, cy = WIDTH / 2, HEIGHT / 2
    max_dist = math.sqrt(cx * cx + cy * cy)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            dist = math.sqrt((x - cx) ** 2 + (y - cy) ** 2) / max_dist
            alpha = int(max(0, min(105, (dist ** 2.2) * 115)))
            px[x, y] = (1, 4, 7, alpha)
    frame.alpha_composite(vignette)


def draw_observatory(draw: ImageDraw.ImageDraw, index: int) -> None:
    """A quiet mission-control frame turns the profile into a place, not a poster."""
    scan_y = 120 + int((index * 22) % 1520)
    draw.line((24, scan_y, WIDTH - 24, scan_y), fill=(88, 166, 255, 32), width=1)
    draw.line((24, scan_y + 1, WIDTH - 24, scan_y + 1), fill=(130, 80, 223, 16), width=1)
    draw.line((34, 122, 34, 1620), fill=(88, 96, 105, 70), width=2)
    draw.line((1166, 122, 1166, 1620), fill=(88, 96, 105, 70), width=2)
    for y in range(155, 1580, 96):
        draw.line((28, y, 40, y), fill=(139, 148, 158, 100), width=2)
        draw.line((1160, y, 1172, y), fill=(139, 148, 158, 100), width=2)
    draw.text((52, 112), "DEEP FIELD / MISSION 01", font=profile_font(14, True), fill=(88, 166, 255, 205))
    draw.text((950, 112), "BANGALORE · UTC+5:30", font=profile_font(13), fill=(139, 148, 158, 190))
    phase = (index / FRAME_COUNT) * math.pi * 2
    signal = int(50 + 28 * (0.5 + 0.5 * math.sin(phase)))
    draw.text((52, 1645), f"SIGNAL {signal:02d}%  /  NOVA NAVIGATION ONLINE", font=profile_font(13, True), fill=(63, 185, 80, 205))
    draw.text((920, 1645), "AYU.OS // THE DEEP FIELD", font=profile_font(13), fill=(139, 148, 158, 185))


def draw_signal_constellations(draw: ImageDraw.ImageDraw, index: int) -> None:
    """Turn selected work into a few intentional data constellations."""
    groups = [
        ([(590, 470), (645, 430), (700, 450), (750, 410)], (88, 166, 255, 155)),
        ([(500, 820), (560, 850), (620, 830), (675, 875)], (130, 80, 223, 145)),
        ([(560, 1180), (630, 1150), (700, 1188), (760, 1140)], (210, 153, 34, 145)),
    ]
    for gi, (points, color) in enumerate(groups):
        draw.line(points, fill=color, width=2)
        pulse_index = (index // 4 + gi) % len(points)
        for pi, (x, y) in enumerate(points):
            radius = 5 if pi == pulse_index else 3
            alpha = 220 if pi == pulse_index else 150
            draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color[:3], alpha))


def draw_transmission(draw: ImageDraw.ImageDraw, index: int) -> None:
    """A warm closing transmission gives the profile a human endpoint."""
    if index < 38:
        return
    pulse = int(90 + 45 * (0.5 + 0.5 * math.sin((index - 38) * 0.45)))
    draw.rounded_rectangle((300, 1545, 900, 1610), radius=30, fill=(31, 35, 40, 240), outline=(210, 153, 34, pulse), width=2)
    draw.text((362, 1568), "OPEN CHANNEL  ·  ALWAYS CURIOUS  ·  SAY HELLO", font=profile_font(17, True), fill=(240, 198, 98, 238))


def draw_cloud(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float, alpha: int = 170) -> None:
    """Build multi-layer moonlit cloud banks with silver linings and transparent depth."""
    cloud = Image.new("RGBA", (300, 145), (0, 0, 0, 0))
    cloud_draw = ImageDraw.Draw(cloud, "RGBA")
    cloud_draw.ellipse((8, 58, 132, 132), fill=(31, 35, 40, alpha))
    cloud_draw.ellipse((74, 22, 194, 132), fill=(47, 54, 64, min(220, alpha + 18)))
    cloud_draw.ellipse((154, 48, 288, 132), fill=(31, 35, 40, alpha))
    cloud_draw.rounded_rectangle((38, 72, 260, 132), radius=30, fill=(47, 54, 64, min(215, alpha + 10)))
    cloud_draw.arc((74, 22, 194, 132), 194, 310, fill=(139, 148, 158, min(170, alpha)), width=3)
    cloud_draw.arc((154, 48, 288, 132), 200, 325, fill=(88, 166, 255, min(130, alpha // 2)), width=2)
    cloud_draw.ellipse((50, 93, 225, 136), fill=(13, 17, 23, max(20, alpha // 2)))
    cloud = cloud.filter(ImageFilter.GaussianBlur(1.2))
    cloud = cloud.resize((int(cloud.width * scale), int(cloud.height * scale)), Image.Resampling.LANCZOS)
    draw._image.alpha_composite(cloud, (x, y))


BASE_BACKGROUND: Image.Image | None = None


def draw_frame(index: int, cat: Image.Image) -> Image.Image:
    global BASE_BACKGROUND
    if BASE_BACKGROUND is None:
        BASE_BACKGROUND = gradient_background().convert("RGBA")
    frame = BASE_BACKGROUND.copy()
    draw = ImageDraw.Draw(frame, "RGBA")

    # Layered atmospheric depth: nebulae, deep stars, and the orbital system.
    draw_nebula(frame, index, 0)
    draw_nebula(frame, index, 1)
    draw_nebula(frame, index, 2)
    draw_deep_stars(draw, index)
    draw_solar_system(draw, index)
    draw_observatory(draw, index)
    draw_signal_constellations(draw, index)

    # Moon halo and soft midnight atmospheric bands.
    for radius, alpha in [(150, 10), (118, 15), (88, 24)]:
        draw.ellipse((1040 - radius, 140 - radius, 1040 + radius, 140 + radius), fill=(88, 166, 255, alpha))
    draw.ellipse((1010, 110, 1070, 170), fill=(240, 246, 252, 245))
    draw.ellipse((1029, 120, 1089, 180), fill=(31, 35, 40, 240))

    # Parallax clouds: distant clouds drift slowly; the foreground cloud crosses
    # the cat's route, making the loop feel like a tiny world rather than a sticker.
    draw_cloud(draw, 80 - (index * 3) % 1450, 310, 0.75, 112)
    draw_cloud(draw, 640 - (index * 6) % 1550, 540, 0.52, 145)
    draw_cloud(draw, 300 - (index * 10) % 1500, 820, 1.15, 165)
    draw_cloud(draw, 870 - (index * 8) % 1500, 1120, 0.68, 125)

    # The planned rails are deliberately quiet so they read as composition, not UI chrome.
    draw_motion_guide(draw, index)
    # Constellation threads and an occasional shooting star.
    constellation = [(160, 240), (222, 188), (284, 230), (340, 168), (405, 218)]
    draw.line(constellation, fill=(88, 166, 255, 120), width=1)
    for x, y in constellation:
        draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill=(240, 246, 252, 230))
    streak_x = (index * 38) % 1320 - 120
    streak_y = 600 - (index * 5) % 300
    draw.line((streak_x, streak_y, streak_x + 80, streak_y - 28), fill=(88, 166, 255, 190), width=2)
    # Distant mountain silhouettes.
    mountain = [(0, 1620), (115, 1500), (220, 1605), (342, 1470), (480, 1610), (610, 1498), (755, 1618), (885, 1488), (1030, 1608), (1130, 1518), (1200, 1605), (1200, 1800), (0, 1800)]
    draw.polygon(mountain, fill=(47, 54, 64, 235))
    draw.polygon([(0, 1690), (170, 1578), (330, 1680), (520, 1555), (700, 1688), (920, 1568), (1200, 1690), (1200, 1800), (0, 1800)], fill=(13, 17, 23, 250))


    # The profile itself is drawn into the canvas so Nova appears to roam
    # around the interface rather than across an empty decorative backdrop.
    draw_profile_copy(draw, index)
    draw_transmission(draw, index)
    draw_vignette(frame)

    # Nova follows a closed, slow choreography. The first and final positions match,
    # so the GIF loops without a teleport at the seam.
    route = [(120, 170), (740, 455), (410, 760), (820, 1110), (220, 1390)]
    segments = [
        (0, 16, "walk", 4, 0),
        (16, 32, "walk", 0, 1),
        (32, 43, "lick", 1, 1),
        (43, 62, "walk", 1, 2),
        (62, 73, "sleep", 2, 2),
        (73, 82, "acro_sleep", 2, 2),
        (82, 91, "wake", 2, 2),
        (91, 104, "walk", 2, 3),
        (104, 114, "greet", 3, 3),
        (114, 117, "walk", 3, 4),
        (117, FRAME_COUNT, "walk", 4, 0),
    ]
    state, start, from_idx, to_idx = segments[-1][2], segments[-1][0], segments[-1][3], segments[-1][4]
    for seg_start, seg_end, seg_state, seg_from, seg_to in segments:
        if seg_start <= index < seg_end:
            state, start, from_idx, to_idx = seg_state, seg_start, seg_from, seg_to
            break
    seg_end = next((item[1] for item in segments if item[0] == start), FRAME_COUNT)
    if state == "walk":
        local = (index - start) / max(1, seg_end - start - 1)
        eased = local * local * (3 - 2 * local)
        x0, y0 = route[from_idx]
        x1, y1 = route[to_idx]
        x = int(x0 + (x1 - x0) * eased)
        y = int(y0 + (y1 - y0) * eased)
    else:
        x, y = route[from_idx]
    phase = index - start
    sprite = pixel_cat(state, phase)
    if state == "acro_sleep":
        sprite = sprite.rotate(-5 + int(10 * math.sin(phase * 0.35)), resample=Image.Resampling.BICUBIC, expand=True)
    elif state == "sleep":
        sprite = sprite.rotate(int(3 * math.sin(phase * 0.28)), resample=Image.Resampling.BICUBIC, expand=True)
    elif state in {"walk", "wake", "greet"}:
        sprite = sprite.rotate(int(1.5 * math.sin(phase * 0.22)), resample=Image.Resampling.BICUBIC, expand=True)
    frame.alpha_composite(sprite, (x, y))

    greeting_text = "hi — welcome to my orbit" if state == "greet" else None
    if greeting_text:
        draw = ImageDraw.Draw(frame, "RGBA")
        pulse = 80 + int(35 * (0.5 + 0.5 * math.sin(phase * 0.35)))
        draw.ellipse((x - 20, y - 20, x + 145, y + 145), outline=(88, 166, 255, pulse), width=3)
        bubble_x = min(WIDTH - 390, max(25, x - 25))
        bubble_y = max(70, y - 78)
        draw.rounded_rectangle((bubble_x, bubble_y, bubble_x + 350, bubble_y + 52), radius=18, fill=(31, 35, 40, 240), outline=(88, 166, 255, 210), width=2)
        draw.polygon([(bubble_x + 44, bubble_y + 52), (bubble_x + 60, bubble_y + 52), (bubble_x + 52, bubble_y + 66)], fill=(31, 35, 40, 240))
        draw.text((bubble_x + 18, bubble_y + 17), greeting_text, font=profile_font(17, True), fill=(240, 246, 252, 245))
    elif state == "sleep":
        draw = ImageDraw.Draw(frame, "RGBA")
        draw.text((x + 95, y - 24), "z", font=profile_font(17, True), fill=(139, 148, 158, 190))

    # A tiny motion trail and status labels keep the scene tied to AYU.OS.
    draw = ImageDraw.Draw(frame, "RGBA")
    draw.line((40, 42, 320, 42), fill=(88, 166, 255, 180), width=2)
    draw.text((40, 56), "AYU.OS / SINGLE-CANVAS PROFILE", fill=(240, 246, 252, 230))
    draw.text((40, 78), "Nova // roaming through the interface", fill=(139, 148, 158, 230))
    draw.text((40, 1730), "NOVA ROUTE COMPLETE · RETURNING TO ORBIT", fill=(139, 148, 158, 220))
    draw.text((1010, 1730), "MOON 01 · ALT 420", fill=(139, 148, 158, 220))
    return frame.convert("RGB")


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Mascot source missing: {SOURCE}")
    cat = make_cat()
    frames = [draw_frame(index, cat) for index in range(FRAME_COUNT)]
    frames[0].save(OUTPUT_GIF, save_all=True, append_images=frames[1:], duration=130, loop=0, optimize=True, disposal=2)
    frames[FRAME_COUNT // 2].save(OUTPUT_STILL, format="PNG", optimize=True)
    print(f"Generated {OUTPUT_GIF}")
    print(f"Generated {OUTPUT_STILL}")


if __name__ == "__main__":
    main()
