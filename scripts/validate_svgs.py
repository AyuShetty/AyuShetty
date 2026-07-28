#!/usr/bin/env python3
"""
AYU.OS SVG Validator
Validates SVGs against COMPONENT_SPEC.md and TOKENS.md requirements.
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS = "http://www.w3.org/2000/svg"

def local_name(tag: str) -> str:
    return tag.split("}", 1)[-1] if "}" in tag else tag

def validate_svg(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, "File missing"
    
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        
        if local_name(root.tag) != "svg":
            return False, "Not an SVG element"
        
        # Check required attributes
        if not root.get("viewBox"):
            return False, "Missing viewBox"
        
        if root.get("role") != "img":
            return False, "Missing role='img'"
        
        # Check required children
        has_title = False
        has_desc = False
        has_style = False
        
        for elem in root.iter():
            tag = local_name(elem.tag)
            if tag == "title":
                has_title = True
            elif tag == "desc":
                has_desc = True
            elif tag == "style" and elem.text and elem.text.strip():
                has_style = True
        
        errors = []
        if not has_title:
            errors.append("Missing <title>")
        if not has_desc:
            errors.append("Missing <desc>")
        if not has_style:
            errors.append("Missing <style> block")
        
        if errors:
            return False, "; ".join(errors)
        
        return True, "PASS"
    except ET.ParseError as e:
        return False, f"XML parse error: {e}"

def validate_directory(dir_path: str) -> list[tuple[str, bool, str]]:
    results = []
    for svg in sorted(Path(dir_path).glob("*.svg")):
        valid, msg = validate_svg(svg)
        results.append((svg.name, valid, msg))
    return results

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="components")
    args = parser.parse_args()
    
    target = Path(args.path)
    if not target.exists():
        print(f"Path not found: {target}")
        sys.exit(1)
    
    results = []
    if target.is_file() and target.suffix == ".svg":
        results = [validate_svg(target)]
    else:
        for subdir in ["primitives", "layouts", "features"]:
            sub = target / subdir
            if sub.exists():
                results.extend(validate_directory(sub))
    
    passed = sum(1 for _, v, _ in results if v)
    failed = len(results) - passed
    
    for name, valid, msg in results:
        status = "PASS" if valid else "FAIL"
        print(f"[{status}] {name}: {msg}")
    
    print(f"\nTotal: {len(results)} | Passed: {passed} | Failed: {failed}")
    
    if failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()