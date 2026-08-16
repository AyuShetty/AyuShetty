"""Build the AYU.OS GitHub profile README and its tracked visual assets.

The public README is intentionally written as normal GitHub-flavoured Markdown.
SVG is generated as standalone files and referenced with relative image links;
raw XML is never embedded in README.md because GitHub renders that as text.
"""
from __future__ import annotations

import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
ASSETS_DIR = ROOT / "assets" / "profile"
DIST_DIR = ROOT / "dist"


def load_json(path: Path) -> dict:
    """Load a JSON data file, returning an empty object when it is absent."""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def text(value: object) -> str:
    """Escape user-controlled values for SVG text nodes."""
    return html.escape(str(value), quote=False)


def attr(value: object) -> str:
    """Escape user-controlled values for SVG attributes."""
    return html.escape(str(value), quote=True)


def build_hero(profile: dict, meta: dict) -> str:
    """Create a static, GitHub-safe hero banner."""
    name = text(profile.get("name", "Ayush N Shetty"))
    title = text(profile.get("title", "Product Engineer"))
    subtitle_value = str(profile.get("subtitle", "AI systems | Ethereum | Developer infrastructure"))
    subtitle_value = subtitle_value.replace("·", " | ").replace("—", "-").replace("&", "and")
    subtitle = text(subtitle_value)
    version = text(meta.get("version", "3.0.0"))
    codename = text(meta.get("codename", "AYU.OS Core"))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" role="img" aria-labelledby="title desc">
  <title id="title">{name} — {title}</title>
  <desc id="desc">{subtitle}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#09090b"/>
      <stop offset="0.62" stop-color="#111827"/>
      <stop offset="1" stop-color="#1c1917"/>
    </linearGradient>
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ef4444"/>
      <stop offset="1" stop-color="#f59e0b" stop-opacity="0"/>
    </linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#ffffff" stroke-opacity="0.055" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="1200" height="300" rx="24" fill="url(#bg)"/>
  <rect x="1" y="1" width="1198" height="298" rx="23" fill="none" stroke="#ffffff" stroke-opacity="0.12"/>
  <rect width="1200" height="300" rx="24" fill="url(#grid)"/>
  <path d="M 0 250 C 260 180, 480 285, 780 205 S 1080 150, 1200 185" fill="none" stroke="url(#glow)" stroke-width="2" opacity="0.9"/>
  <rect x="72" y="54" width="7" height="192" rx="3.5" fill="#ef4444"/>
  <circle cx="1030" cy="74" r="5" fill="#22c55e"/>
  <text x="1050" y="80" fill="#a1a1aa" font-family="Courier New, Courier, monospace" font-size="14" letter-spacing="2">ONLINE / {version}</text>
  <text x="112" y="105" fill="#f8fafc" font-family="Arial, Helvetica, sans-serif" font-size="38" font-weight="700">{name}</text>
  <text x="112" y="148" fill="#fca5a5" font-family="Courier New, Courier, monospace" font-size="17" letter-spacing="1">{title.upper()}  /  {codename}</text>
  <text x="112" y="196" fill="#cbd5e1" font-family="Arial, Helvetica, sans-serif" font-size="17">{subtitle}</text>
  <text x="112" y="236" fill="#94a3b8" font-family="Courier New, Courier, monospace" font-size="13">BUILDING USEFUL SYSTEMS AT THE EDGE OF AI, WEB3, AND PRODUCT ENGINEERING</text>
</svg>
'''


def write_assets(profile: dict, meta: dict) -> None:
    """Refresh only the tracked profile asset directory."""
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    (ASSETS_DIR / "hero.svg").write_text(build_hero(profile, meta), encoding="utf-8")


def project_rows(projects: dict) -> list[str]:
    rows = []
    for project in projects.get("featured", []):
        if not project.get("featured", True):
            continue
        title = project.get("title", project.get("name", "Project"))
        repo = project.get("repo_url", "")
        demo = project.get("demo_url", "")
        links = [f"[Repo]({repo})"] if repo else []
        if demo:
            links.append(f"[Demo]({demo})")
        stack = " · ".join(f"`{item}`" for item in project.get("tech_stack", [])[:6])
        description = project.get("description", "").replace("|", "\\|")
        rows.append(f"| **[{title}]({repo})** | {description} | {stack} | {' · '.join(links)} |")
    return rows


def experience_rows(experience: dict) -> list[str]:
    rows = []
    for position in experience.get("positions", [])[:3]:
        end = "Present" if position.get("current") else position.get("end", "")
        period = f"{position.get('start', '')} – {end}"
        company = position.get("company", "")
        role = position.get("role", "")
        summary = position.get("description", "").replace("|", "\\|")
        rows.append(f"| **{role}**<br>{company} | {period} | {summary} |")
    return rows


def objective_rows(objectives: dict) -> list[str]:
    rows = []
    for objective in objectives.get("objectives", [])[:4]:
        title = objective.get("title", "Objective")
        progress = objective.get("progress", "—")
        description = objective.get("description", "").replace("|", "\\|")
        rows.append(f"| **{title}** | `{progress}%` | {description} |")
    return rows


def contact_rows(contact: dict) -> list[str]:
    rows = []
    for channel in contact.get("channels", []):
        label = channel.get("channel", "Contact")
        handle = channel.get("handle", label)
        url = channel.get("url", "")
        if url:
            rows.append(f"| **{label}** | [{handle}]({url}) |")
    return rows


def build_readme(data: dict) -> str:
    profile = data["profile"]
    meta = data["meta"]
    skills = data["skills"]
    projects = data["projects"]
    experience = data["experience"]
    objectives = data["objectives"]
    contact = data["contact"]
    stats = data["stats"]

    language_items = []
    for category in skills.get("categories", []):
        items = [f"`{item.get('name', '')}`" for item in category.get("items", [])]
        if items:
            language_items.append(f"| **{category.get('name', 'Stack')}** | {' · '.join(items)} |")

    stats_rows = [
        f"| Public repositories | **{stats.get('public_repos', '—')}** |",
        f"| Stars / forks | **{stats.get('total_stars', '—')} / {stats.get('total_forks', '—')}** |",
        f"| Commits in the latest period | **{stats.get('total_commits_1y', '—')}** |",
        f"| Followers | **{stats.get('followers', '—')}** |",
    ]

    focus_rows = [
        "| **AI systems** | Local LLM orchestration, browser agents, workflow automation, and human-in-the-loop tooling. |",
        "| **Ethereum** | Governance analytics, EIP diagnostics, protocol tooling, and verifiable learning experiences. |",
        "| **Product engineering** | Full-stack systems, developer infrastructure, design systems, and reliable delivery. |",
        "| **Security research** | Biometric key derivation, MPC/TSS exploration, and privacy-preserving local-first systems. |",
    ]

    lines = [
        '<p align="center"><img src="assets/profile/sky-cat.gif" alt="Animated AYU.OS Deep Field observatory with parallax nebulae, orbital systems, illuminated data constellations, mission framing, and Nova greeting visitors" width="100%"></p>',
        '<p align="center"><sub>Nova, the AYU.OS navigator · Deep Field mission log · stops to greet visitors · <a href="assets/profile/sky-cat-still.png">static frame</a></sub></p>',
        "",
        "<details>",
        "<summary>Open accessible text profile, links, and project details</summary>",
        "",
        f"# {profile.get('name', 'Ayush N Shetty')}",
        f"**{profile.get('title', 'Product Engineer')}** · {profile.get('location', 'Bangalore, India')} · {profile.get('timezone', 'UTC+5:30')}",
        "",
        profile.get("bio", ""),
        "",
        f"[Portfolio]({profile.get('website', 'https://ayushetty.me')}) · [GitHub](https://github.com/AyuShetty) · [LinkedIn](https://linkedin.com/in/ayushetty) · [X](https://x.com/AyuShettyEth)",
        "",
        "> **System status:** online. Open to interesting problems across AI infrastructure, Ethereum protocols, and developer experience.",
        "",
        '<p align="center"><img src="assets/profile/sky-divider.svg" alt="" width="100%"></p>',
        "",
        "## What I build",
        "",
        "| Focus | Current direction |",
        "| --- | --- |",
        *focus_rows,
        "",
        '<p align="center"><img src="assets/profile/sky-divider.svg" alt="" width="100%"></p>',
        "",
        "## Selected work",
        "",
        "The strongest projects are intentionally presented as products rather than a catalogue of every experiment.",
        "",
        "| Project | What it does | Stack | Links |",
        "| --- | --- | --- | --- |",
        *project_rows(projects),
        "",
        '<p align="center"><img src="assets/profile/sky-divider.svg" alt="" width="100%"></p>',
        "",
        "## Technical range",
        "",
        "| Area | Tools and technologies |",
        "| --- | --- |",
        *language_items,
        "",
        '<p align="center"><img src="assets/profile/sky-divider.svg" alt="" width="100%"></p>',
        "",
        "## Experience",
        "",
        "| Role | Period | Scope |",
        "| --- | --- | --- |",
        *experience_rows(experience),
        "",
        '<p align="center"><img src="assets/profile/sky-divider.svg" alt="" width="100%"></p>',
        "",
        "## Current objectives",
        "",
        "| Objective | Progress | Direction |",
        "| --- | ---: | --- |",
        *objective_rows(objectives),
        "",
        '<p align="center"><img src="assets/profile/sky-divider.svg" alt="" width="100%"></p>',
        "",
        "## GitHub telemetry",
        "",
        "| Metric | Snapshot |",
        "| --- | ---: |",
        *stats_rows,
        "",
        '<p align="center"><img src="assets/profile/sky-divider.svg" alt="" width="100%"></p>',
        "",
        "## Connect",
        "",
        "| Channel | Link |",
        "| --- | --- |",
        *contact_rows(contact),
        "",
        "---",
        "",
        f"> {profile.get('tagline', 'Shipping real products. Exploring MPC/TSS security. Code that actually scales.')}",
        ">",
        f"> AYU.OS profile build **v{meta.get('version', '3.0.0')}** · The README is generated from [`data/`](data/) and the visual system lives in [`components/`](components/).",
        "",
        "<p align=\"center\"><sub>Built with care in Bangalore. Designed to be useful before it is impressive.</sub></p>",
        "",
        "</details>",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    profile = load_json(DATA_DIR / "profile.json")
    meta = profile.get("meta", {})
    data = {
        "profile": profile,
        "meta": meta,
        "skills": load_json(DATA_DIR / "skills.json"),
        "projects": load_json(DATA_DIR / "projects.json"),
        "experience": load_json(DATA_DIR / "experience.json"),
        "objectives": load_json(DATA_DIR / "objectives.json"),
        "contact": load_json(DATA_DIR / "contact.json"),
        "stats": load_json(DATA_DIR / "stats.json"),
    }

    write_assets(profile, meta)
    readme = build_readme(data)
    (ROOT / "README.md").write_text(readme, encoding="utf-8")

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    (DIST_DIR / "README.md").write_text(readme, encoding="utf-8")
    dist_assets = DIST_DIR / "assets" / "profile"
    if dist_assets.exists():
        shutil.rmtree(dist_assets)
    dist_assets.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ASSETS_DIR / "hero.svg", dist_assets / "hero.svg")

    print("AYU.OS profile build complete")
    print(f"  README: {ROOT / 'README.md'}")
    print(f"  Assets: {ASSETS_DIR}")
    print(f"  Version: {meta.get('version', '3.0.0')}")


if __name__ == "__main__":
    main()
