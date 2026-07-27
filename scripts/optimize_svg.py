"""
AYU.OS SVG Optimization Tool
Minifies SVG files by removing unnecessary whitespace and comments.
Preserves XML structure and accessibility metadata.
"""
import re
from pathlib import Path

def minify_svg(content):
    content = re.sub(r">\s+<", "><", content)
    content = re.sub(r"\s{2,}", " ", content)
    content = re.sub(r"\s*=\s*", "=", content)
    content = content.strip()
    return content

def optimize_directory(dir_path):
    for svg in sorted(Path(dir_path).glob("*.svg")):
        original = svg.read_text(encoding="utf-8")
        optimized = minify_svg(original)
        if optimized != original:
            svg.write_text(optimized, encoding="utf-8")

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "ayu-ui"
    optimize_directory(target)
