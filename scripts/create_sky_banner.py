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
FRAME_COUNT = 48


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
    mascot.thumbnail((210, 210), Image.Resampling.LANCZOS)
    return mascot


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


def draw_profile_copy(draw: ImageDraw.ImageDraw) -> None:
    draw_panel(draw, 40, 155, 550, 265, "AYU.OS / IDENTITY", [
        "AYUSH N SHETTY",
        "Product Engineer · Bangalore · UTC+5:30",
        "iOS + blockchain builder shipping real products.",
        "Exploring MPC/TSS security, AI infrastructure,",
        "hackathons, product thinking, and design refinement.",
        "SYSTEM STATUS  //  ONLINE",
    ], accent=(88, 166, 255, 235))
    draw_panel(draw, 40, 480, 520, 260, "WHAT I BUILD", [
        "AI SYSTEMS       local LLMs · agents",
        "ETHEREUM         governance · EIPs",
        "PRODUCT          full-stack · DX",
        "SECURITY         MPC/TSS · privacy",
        "FOCUS            useful before impressive",
    ], accent=(88, 166, 255, 235))
    draw_panel(draw, 640, 480, 520, 340, "SELECTED WORK", [
        "ETH.ED           Web3 learning platform",
        "EIPSINSIGHT      governance analytics",
        "FACIAL KEYGEN    biometric key research",
        "AIRGESTURE       touchless control",
        "ETHERWORLD IOS   scalable app architecture",
        "THIS PORTFOLIO   immersive 3D experience",
        "AYU.OS           profile as an operating system",
    ], accent=(210, 153, 34, 235))
    draw_panel(draw, 40, 800, 520, 330, "TECHNICAL RANGE", [
        "TypeScript · Python · Solidity · Swift",
        "Next.js · React · SwiftUI · Three.js",
        "Docker · Kubernetes · AWS/GCP · PostgreSQL",
        "Ollama · Playwright · LangGraph · OpenCV",
        "Ethereum · ENS · Foundry · Hardhat",
        "Agents · DX · Design systems · WebGL",
    ], accent=(63, 185, 80, 235))
    draw_panel(draw, 640, 880, 520, 265, "EXPERIENCE", [
        "PRODUCT ENGINEER     Avarch · 2023–Present",
        "PRESIDENT             COPE · 2022–2023",
        "SOFTWARE INTERN       Avarch · 2021–2022",
        "Building Web3 + AI platforms and communities.",
    ], accent=(130, 80, 223, 235))
    draw_panel(draw, 40, 1200, 520, 340, "CURRENT OBJECTIVES", [
        "LOCAL AI INFRA v1       65%",
        "EIPSINSIGHT v2          15%",
        "AYU.OS OPEN SOURCE      40%",
        "FACIAL KEYGEN RESEARCH  30%",
        "Distributed inference, governance intelligence,",
        "plugin architecture, and post-quantum research.",
    ], accent=(207, 34, 46, 235))
    draw_panel(draw, 640, 1210, 520, 300, "TELEMETRY / CONNECT", [
        "19 PUBLIC REPOSITORIES",
        "4 STARS  ·  2 FORKS  ·  368 COMMITS",
        "3 FOLLOWERS",
        "ayushetty.me",
        "github.com/AyuShetty",
        "linkedin.com/in/ayushetty  ·  @AyuShettyEth",
    ], accent=(88, 166, 255, 235))


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
    """Paint a soft, slowly shifting nebula layer for atmospheric depth."""
    haze = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    haze_draw = ImageDraw.Draw(haze, "RGBA")
    centers = [(260, 560), (920, 1040), (330, 1440)]
    cx, cy = centers[layer % len(centers)]
    drift = int(22 * math.sin(index / FRAME_COUNT * math.pi * 2 + layer))
    for radius, alpha in [(310, 8), (230, 11), (150, 16)]:
        haze_draw.ellipse((cx + drift - radius, cy - radius, cx + drift + radius, cy + radius), fill=(47, 67, 89, alpha))
    haze = haze.filter(ImageFilter.GaussianBlur(36))
    frame.alpha_composite(haze)


def draw_deep_stars(draw: ImageDraw.ImageDraw, index: int) -> None:
    """Use several parallax star fields instead of one flat random field."""
    for layer, count in [(0, 42), (1, 30), (2, 18)]:
        random.seed(100 + layer)
        drift = int((index * (layer + 1) * 2.3) % WIDTH)
        for _ in range(count):
            x = (random.randint(0, WIDTH - 1) + drift) % WIDTH
            y = random.randint(20, 1450)
            r = random.choice([1, 1, 1, 2]) if layer < 2 else 2
            twinkle = int(130 + 100 * (0.5 + 0.5 * math.sin(index * 0.55 + x)))
            draw.ellipse((x - r, y - r, x + r, y + r), fill=(201, 209, 217, twinkle))


def draw_solar_system(draw: ImageDraw.ImageDraw, index: int) -> None:
    """Render a small orbital system with stable geometry and gentle motion."""
    cx, cy = 815, 285
    for radius in (68, 108, 148):
        draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), outline=(88, 96, 105, 88), width=2)
    draw.ellipse((cx - 32, cy - 32, cx + 32, cy + 32), fill=(210, 153, 34, 245), outline=(240, 198, 98, 220), width=3)
    draw.ellipse((cx - 20, cy - 20, cx + 20, cy + 20), fill=(240, 198, 98, 220))
    planets = [(68, 7, (88, 166, 255, 240), 1.0), (108, 10, (130, 80, 223, 240), -0.7), (148, 14, (63, 185, 80, 240), 0.45)]
    for radius, size, color, speed in planets:
        angle = index / FRAME_COUNT * math.pi * 2 * speed + radius / 90
        px = int(cx + math.cos(angle) * radius)
        py = int(cy + math.sin(angle) * radius * 0.58)
        draw.ellipse((px - size, py - size, px + size, py + size), fill=color)
        if radius == 108:
            draw.ellipse((px - size - 8, py - 3, px + size + 8, py + 3), outline=(130, 80, 223, 160), width=2)
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
    fill = (88, 96, 105, alpha)
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
    draw_profile_copy(draw)
    draw_transmission(draw, index)
    draw_vignette(frame)

    # Nova follows a planned multi-stop route.
    # Each stop has a short hold, a
    # gentle settling motion, and a greeting bubble so the mascot behaves like a
    # host rather than a sticker sliding on a rail.
    route = [(120, 170), (740, 455), (410, 760), (820, 1110), (220, 1390)]
    greeting_windows = {range(6, 12): "hi — welcome to my orbit", range(22, 29): "thanks for stopping by", range(38, 46): "let's build something real"}
    active_greeting = next((text for window, text in greeting_windows.items() if index in window), None)
    # Reserve real time for each stop: travel occupies the gaps, greetings occupy
    # several frames, and the mascot settles with a small breathing motion.
    stop_centers = {8: route[1], 24: route[3], 40: route[4]}
    if active_greeting:
        nearest = min(stop_centers, key=lambda stop: abs(stop - index))
        x, y = stop_centers[nearest]
    else:
        segment = index / (FRAME_COUNT - 1) * (len(route) - 1)
        stop_index = min(len(route) - 1, int(segment))
        local = segment - stop_index
        easing = local * local * (3 - 2 * local)
        x0, y0 = route[stop_index]
        x1, y1 = route[min(stop_index + 1, len(route) - 1)]
        x = int(x0 + (x1 - x0) * easing + 10 * math.sin(index * 0.35))
        y = int(y0 + (y1 - y0) * easing + 8 * math.sin(index * 0.5))
    bob = 2.5 * math.sin(index * 0.42) if not active_greeting else 0.8 * math.sin(index * 0.5)
    bobbed = cat.rotate(bob, resample=Image.Resampling.BICUBIC, expand=True)
    frame.alpha_composite(bobbed, (x, y))

    if active_greeting:
        draw = ImageDraw.Draw(frame, "RGBA")
        draw.ellipse((x - 20, y - 20, x + 205, y + 205), outline=(88, 166, 255, 90), width=3)
        draw.ellipse((x - 32, y - 32, x + 217, y + 217), outline=(63, 185, 80, 40), width=2)
        bubble_x = min(WIDTH - 390, max(25, x - 25))
        bubble_y = max(70, y - 78)
        draw.rounded_rectangle((bubble_x, bubble_y, bubble_x + 350, bubble_y + 52), radius=18, fill=(31, 35, 40, 240), outline=(88, 166, 255, 210), width=2)
        draw.polygon([(bubble_x + 44, bubble_y + 52), (bubble_x + 60, bubble_y + 52), (bubble_x + 52, bubble_y + 66)], fill=(31, 35, 40, 240))
        draw.text((bubble_x + 18, bubble_y + 17), active_greeting, font=profile_font(17, True), fill=(240, 246, 252, 245))

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
    frames[0].save(OUTPUT_GIF, save_all=True, append_images=frames[1:], duration=105, loop=0, optimize=True, disposal=2)
    frames[FRAME_COUNT // 2].save(OUTPUT_STILL, format="PNG", optimize=True)
    print(f"Generated {OUTPUT_GIF}")
    print(f"Generated {OUTPUT_STILL}")


if __name__ == "__main__":
    main()
