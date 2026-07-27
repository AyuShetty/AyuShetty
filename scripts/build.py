
import sys
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GENERATED = ROOT / "generated"
sys.path.insert(0, str(ROOT / "scripts"))

def load_template(name):
    path = ROOT / "templates" / f"{name}.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")

def render_template(template, context):
    for key, value in context.items():
        template = template.replace("{{" + key + "}}", str(value))
    return template

def build_readme(version, modules, terminal, logs, projects, research, timeline, stats, contributions, skills, objectives, contact):
    header = load_template("header")
    kernel = load_template("kernel")
    modules_tpl = load_template("modules")
    profile = load_template("profile")
    projects_tpl = load_template("projects")
    research_tpl = load_template("research")
    timeline_tpl = load_template("timeline")
    stats_tpl = load_template("stats")
    contributions_tpl = load_template("contributions")
    skills_tpl = load_template("skills")
    objectives_tpl = load_template("objectives")
    contact_tpl = load_template("contact")
    terminal_tpl = load_template("terminal")
    footer = load_template("footer")

    modules_rows = "\n".join(
        [f"| {m['name']} | {m['status']} | {m['desc']} |" for m in modules]
    )

    projects_rows = "\n".join(
        [f"- **{p['name']}** — {p['desc']}" for p in projects]
    )

    research_rows = "\n".join(
        [f"- **{r['name']}** — {r['desc']}" for r in research]
    )

    timeline_rows = "\n".join(
        [f"- **{t['period']}** — {t['desc']}" for t in timeline]
    )

    contributions_rows = "\n".join(
        [f"- **{c['repo']}** ({c['type']}): {c['desc']}" for c in contributions]
    )

    skills_rows = "\n".join(
        [f"**{s['category']}**\n- {s['items']}" for s in skills]
    )

    objectives_rows = "\n".join(
        [f"- {o}" for o in objectives]
    )

    contact_rows = "\n".join(
        [f"- **{c['channel']}**: {c['handle']}" for c in contact]
    )

    context = {
        "version": version["version"],
        "codename": version["codename"],
        "modules": modules_rows,
        "terminal_about": terminal["about"],
        "terminal_help": terminal["help"],
        "terminal_output": terminal.get("output", ""),
        "logs": "\n".join([f"- `{l['time']}` [{l['level']}] {l['msg']}" for l in logs]),
        "projects": projects_rows,
        "research": research_rows,
        "timeline": timeline_rows,
        "repositories": stats.get("repositories", ""),
        "stars": stats.get("stars", ""),
        "commits": stats.get("commits", ""),
        "followers": stats.get("followers", ""),
        "following": stats.get("following", ""),
        "contributions": contributions_rows,
        "skills": skills_rows,
        "objectives": objectives_rows,
        "contact": contact_rows,
    }

    readme = f"""<div align="center">
  <img src="assets/cyber_hud.svg" width="100%" alt="AYU.OS Core HUD" />
</div>

{render_template(header, context)}

---

## Mission Control

{render_template(modules_tpl, context)}

---

## Developer Profile

{render_template(profile, context)}

---

## Skills

{render_template(skills_tpl, context)}

---

## Projects

{render_template(projects_tpl, context)}

---

## Research

{render_template(research_tpl, context)}

---

## Timeline

{render_template(timeline_tpl, context)}

---

## Current Objectives

{render_template(objectives_tpl, context)}

---

## Contact

{render_template(contact_tpl, context)}

---

## Terminal

```text
{context['terminal_output']}
```

---

## Kernel Status

{render_template(kernel, context)}

{render_template(footer, context)}
"""
    return readme

def copy_assets():
    src_assets = ROOT / "assets"
    dst_assets = GENERATED / "assets"
    if dst_assets.exists():
        shutil.rmtree(dst_assets)
    shutil.copytree(src_assets, dst_assets)

def validate_svgs():
    from generate_svg import validate_directory
    results = []
    for dir_name in ["ayu-ui", "assets/ui", "assets/icons"]:
        dir_path = ROOT / dir_name
        if dir_path.exists():
            results.extend(validate_directory(dir_path))
    return results

def optimize_svgs():
    from optimize_svg import optimize_directory
    for dir_name in ["ayu-ui", "assets/ui", "assets/icons"]:
        dir_path = ROOT / dir_name
        if dir_path.exists():
            optimize_directory(dir_path)

def build():
    GENERATED.mkdir(exist_ok=True)

    from generate_version import get_version
    from generate_modules import get_modules
    from generate_terminal import get_commands, get_terminal_output
    from generate_logs import get_logs
    from generate_stats import get_stats
    from generate_projects import get_projects
    from generate_contributions import get_contributions
    from generate_skills import get_skills
    from generate_objectives import get_objectives
    from generate_contact import get_contact

    version = get_version()
    modules = get_modules()
    terminal = get_commands()
    terminal["output"] = get_terminal_output()
    logs = get_logs()
    stats = get_stats()
    projects = get_projects()
    contributions = get_contributions()
    skills = get_skills()
    objectives = get_objectives()
    contact = get_contact()

    research = [
        {"name": "Artificial Intelligence", "desc": "Local LLM orchestration, agent design, reasoning engines."},
        {"name": "Ethereum", "desc": "Protocol analysis, EIP research, on-chain tooling."},
        {"name": "Systems Design", "desc": "Distributed systems, developer infrastructure, automation."},
        {"name": "Design Systems", "desc": "Component architecture, SVG engineering, token-driven UI."},
    ]

    timeline = [
        {"period": "Present", "desc": "Product Engineer, focusing on AI browser agents and Ethereum protocols."},
        {"period": "Past", "desc": "B.Tech Information Science & Engineering."},
    ]

    svg_results = validate_svgs()
    failures = [r for r in svg_results if not r[1]]
    if failures:
        print("SVG validation failures:")
        for name, valid, msg in failures:
            print(f"  [FAIL] {name}: {msg}")
        sys.exit(1)

    readme = build_readme(version, modules, terminal, logs, projects, research, timeline, stats, contributions, skills, objectives, contact)
    (GENERATED / "README.md").write_text(readme, encoding="utf-8")

    copy_assets()
    optimize_svgs()

    print(f"Build complete. Version {version['version']}")
    print(f"Generated: {GENERATED / 'README.md'}")

if __name__ == "__main__":
    build()
