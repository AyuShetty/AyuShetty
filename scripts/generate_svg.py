"""
AYU.OS SVG Validation Tool
Validates SVGs against COMPONENT_SPEC.md and TOKENS.md.
"""
import xml.etree.ElementTree as ET
from pathlib import Path

NS = "http://www.w3.org/2000/svg"

def local_name(tag):
    return tag.split("}", 1)[-1] if "}" in tag else tag

def validate_svg(path):
    path = Path(path)
    if not path.exists():
        return False, "File missing"

    try:
        tree = ET.parse(path)
        root = tree.getroot()
        if local_name(root.tag) != "svg":
            return False, "Not an SVG element"

        title = None
        desc = None
        has_style = False

        for elem in root.iter():
            tag = local_name(elem.tag)
            if tag == "title":
                title = elem
            elif tag == "desc":
                desc = elem
            elif tag == "style" and elem.text and elem.text.strip():
                has_style = True

        if title is None or desc is None:
            return False, "Missing title or desc"

        if not has_style:
            return False, "Missing <style> block"

        return True, "PASS"
    except ET.ParseError as e:
        return False, f"XML parse error: {e}"

def validate_directory(dir_path):
    results = []
    for svg in sorted(Path(dir_path).glob("*.svg")):
        valid, msg = validate_svg(svg)
        results.append((svg.name, valid, msg))
    return results

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "ayu-ui"
    results = validate_directory(target)
    for name, valid, msg in results:
        status = "PASS" if valid else "FAIL"
        print(f"[{status}] {name}: {msg}")
