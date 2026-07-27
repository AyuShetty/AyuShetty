
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GENERATED = ROOT / "generated"

def load_template(name):
    path = ROOT / "templates" / f"{name}.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")

def render_template(template, context):
    for key, value in context.items():
        template = template.replace("{{" + key + "}}", str(value))
    return template

def build_readme(version, modules, terminal, stats, logs):
    header = load_template("header")
    footer = load_template("footer")
    kernel = load_template("kernel")
    modules_tpl = load_template("modules")
    network = load_template("network")
    terminal_tpl = load_template("terminal")

    context = {
        "version": version["version"],
        "codename": version["codename"],
        "modules": "\n".join([f"| {m['name']} | {m['status']} | {m['desc']} |" for m in modules]),
        "skills": "Python | TypeScript | Solidity | Playwright | Ollama | Docker",
        "terminal_help": terminal["help"],
        "terminal_about": terminal["about"],
        "repos": stats["repositories"],
        "stars": stats["stars"],
        "commits": stats["commits"],
        "logs": "\n".join([f"- `{l['time']}` [{l['level']}] {l['msg']}" for l in logs])
    }

    readme = f"""<div align="center">
  <img src="assets/cyber_hud.svg" width="100%" alt="AYU.OS Core HUD" />
</div>

{render_template(header, context)}

---

## Mission Control

{render_template(modules_tpl, context)}

---

## Kernel Status

{render_template(kernel, context)}

---

## System Telemetry

- Repositories: **{stats['repositories']}**
- Stars: **{stats['stars']}**
- Commits: **{stats['commits']}**

---

## Terminal

```text
{terminal['output']}
```

---

{render_template(footer, context)}
"""
    return readme

def copy_assets():
    src_assets = ROOT / "assets"
    dst_assets = GENERATED / "assets"
    if dst_assets.exists():
        shutil.rmtree(dst_assets)
    shutil.copytree(src_assets, dst_assets)

def build():
    GENERATED.mkdir(exist_ok=True)

    from generate_version import get_version
    from generate_modules import get_modules
    from generate_terminal import get_commands, get_terminal_output
    from generate_stats import get_stats
    from generate_logs import get_logs

    version = get_version()
    modules = get_modules()
    terminal = get_commands()
    terminal["output"] = get_terminal_output()
    stats = get_stats()
    logs = get_logs()

    readme = build_readme(version, modules, terminal, stats, logs)
    (GENERATED / "README.md").write_text(readme, encoding="utf-8")

    copy_assets()

    print(f"Build complete. Version {version['version']}")
    print(f"Generated: {GENERATED / 'README.md'}")

if __name__ == "__main__":
    build()
