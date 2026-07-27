
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {"svg": "http://www.w3.org/2000/svg"}

def validate_svg(path):
    path = Path(path)
    if not path.exists():
        return False
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        if not root.tag.endswith("svg"):
            return False
        title = root.find("svg:title", NS)
        desc = root.find("svg:desc", NS)
        if title is None or desc is None:
            return False
        return True
    except ET.ParseError:
        return False

def validate_directory(dir_path):
    results = []
    for svg in Path(dir_path).glob("*.svg"):
        valid = validate_svg(svg)
        results.append((svg.name, valid))
    return results

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "ayu-ui"
    results = validate_directory(target)
    for name, valid in results:
        status = "PASS" if valid else "FAIL"
        print(f"[{status}] {name}")
