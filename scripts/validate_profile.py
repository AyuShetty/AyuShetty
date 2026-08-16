"""Validate the generated GitHub profile without network access."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_urls(value: object) -> list[str]:
    urls: list[str] = []
    if isinstance(value, dict):
        for item in value.values():
            urls.extend(collect_urls(item))
    elif isinstance(value, list):
        for item in value:
            urls.extend(collect_urls(item))
    elif isinstance(value, str) and value.startswith(("http://", "https://")):
        urls.append(value)
    return urls


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def main() -> None:
    data_dir = ROOT / "data"
    for path in sorted(data_dir.glob("*.json")):
        try:
            load_json(path)
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON in {path}: {exc}")

    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "<svg" in readme.lower() or "<?xml" in readme.lower():
        fail("README.md contains raw SVG/XML; use a linked asset instead")
    required_assets = {
        "assets/profile/sky-cat.gif": "animated sky banner",
        "assets/profile/sky-cat-still.png": "static sky fallback",
        "assets/profile/sky-divider.svg": "sky divider",
    }
    for relative_path, label in required_assets.items():
        if relative_path not in readme:
            fail(f"README.md does not reference {label}: {relative_path}")
        if not (ROOT / relative_path).exists():
            fail(f"{label} is missing: {relative_path}")
    if re.search(r"\]\(\s*\)", readme):
        fail("README.md contains an empty Markdown link")

    for path in sorted(data_dir.glob("*.json")):
        for url in collect_urls(load_json(path)):
            parsed = urlparse(url)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                fail(f"invalid URL in {path}: {url}")

    # Every AyuShetty GitHub repository link used by the profile must be a valid
    # repository-shaped URL. Network reachability is checked in a separate job
    # when credentials and rate limits are available.
    for url in re.findall(r"https://github\.com/AyuShetty/[A-Za-z0-9_.-]+", readme):
        if url.endswith("/AyuShetty"):
            continue
        if urlparse(url).path.count("/") < 2:
            fail(f"malformed GitHub repository URL: {url}")

    print("[PASS] JSON data, README safety checks, and profile asset checks")


if __name__ == "__main__":
    main()
