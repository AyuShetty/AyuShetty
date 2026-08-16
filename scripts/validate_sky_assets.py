"""Validate generated sky assets using only the Python standard library."""
from __future__ import annotations

import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSET_DIR = ROOT / "assets" / "profile"
EXPECTED_SIZE = (1200, 420)


def gif_info(path: Path) -> tuple[tuple[int, int], int]:
    data = path.read_bytes()
    if data[:6] not in {b"GIF87a", b"GIF89a"}:
        raise SystemExit("sky-cat.gif is not a GIF")
    width, height = struct.unpack_from("<HH", data, 6)
    # Each rendered GIF frame begins with an image separator. This is a small,
    # dependency-free sanity check rather than a full GIF decoder.
    frame_count = data.count(b"\x2c")
    return (width, height), frame_count


def png_info(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("sky-cat-still.png is not a PNG")
    width, height = struct.unpack_from(">II", data, 16)
    return width, height


def main() -> None:
    gif_size, frame_count = gif_info(ASSET_DIR / "sky-cat.gif")
    still_size = png_info(ASSET_DIR / "sky-cat-still.png")
    if gif_size != EXPECTED_SIZE or still_size != EXPECTED_SIZE:
        raise SystemExit(f"sky assets have unexpected dimensions: {gif_size}, {still_size}")
    if frame_count < 2:
        raise SystemExit("sky-cat.gif is not animated")
    print(f"[PASS] sky-cat.gif has at least {frame_count} image frames at {gif_size}; static fallback is {still_size}")


if __name__ == "__main__":
    main()
