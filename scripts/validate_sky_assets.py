"""Validate the generated sky assets used by the profile README."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ASSET_DIR = ROOT / "assets" / "profile"


def main() -> None:
    gif = Image.open(ASSET_DIR / "sky-cat.gif")
    still = Image.open(ASSET_DIR / "sky-cat-still.png")
    if gif.format != "GIF" or getattr(gif, "n_frames", 1) < 2:
        raise SystemExit("sky-cat.gif is not animated")
    if gif.size != (1200, 420) or still.size != (1200, 420):
        raise SystemExit("sky assets have unexpected dimensions")
    print(f"[PASS] sky-cat.gif has {gif.n_frames} frames at {gif.size}; static fallback is {still.size}")


if __name__ == "__main__":
    main()
