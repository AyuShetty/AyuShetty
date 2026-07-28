#!/usr/bin/env python3
"""
AYU.OS Build System v2.0
Builds the GitHub profile README from data-driven templates and SVG components.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime
from string import Template
import re

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
COMPONENTS_DIR = ROOT / "components"
DIST_DIR = ROOT / "dist"
ASSETS_DIR = DIST_DIR / "assets"
ROOT_README = ROOT / "README.md"
ROOT_ASSETS = ROOT / "assets"

def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"  ⚠ Error parsing {path}: {e}")
        return {}

def render_template(template_str: str, context: dict) -> str:
    """Simple template rendering with {{VAR}} substitution."""
    def replace_var(match):
        key = match.group(1).strip()
        # Handle nested keys like profile.name
        keys = key.split('.')
        value = context
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, '')
            else:
                value = ''
                break
        return str(value) if value is not None else ''
    
    return re.sub(r'\{\{([^}]+)\}\}', replace_var, template_str)

def load_svg_component(component_path: Path) -> str:
    """Load an SVG component file."""
    if component_path.exists():
        return component_path.read_text(encoding="utf-8")
    return ""

def render_section_header(title: str, subtitle: str) -> str:
    """Render a section header SVG with given title and subtitle."""
    svg_template = COMPONENTS_DIR / "primitives" / "header.svg"
    if not svg_template.exists():
        # Fallback inline
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 80" role="img">
  <title>{title}</title>
  <desc>Section header for {title}: {subtitle}</desc>
  <defs>
    <style>
      .ayu-surface {{ fill: #09090B; }}
      .ayu-border {{ fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }}
      .ayu-accent {{ fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }}
      .ayu-separator {{ stroke: #27272A; stroke-width: 1.5; }}
      .ayu-text-primary {{ fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 14px; font-weight: 600; }}
      .ayu-text-muted {{ fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; }}
    </style>
  </defs>
  <rect class="ayu-surface" width="1000" height="80" rx="12"/>
  <rect class="ayu-border" width="1000" height="80" rx="12"/>
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 68 L 28 52 L 12 52"/>
    <path class="ayu-accent" d="M 972 68 L 972 52 L 988 52"/>
  </g>
  <line class="ayu-separator" x1="32" y1="52" x2="968" y2="52"/>
  <text class="ayu-text-primary" x="40" y="36">{title}</text>
  <text class="ayu-text-muted" x="40" y="56">{subtitle}</text>
</svg>"""
    
    svg_content = svg_template.read_text(encoding="utf-8")
    svg_content = render_template(svg_content, {"TITLE": title, "SUBTITLE": subtitle})
    return svg_content

def render_boot_sequence(version: str, codename: str, module_count: int) -> str:
    """Render the boot sequence SVG."""
    svg_template = COMPONENTS_DIR / "primitives" / "boot-sequence.svg"
    if svg_template.exists():
        svg_content = svg_template.read_text(encoding="utf-8")
    else:
        svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 120" role="img">
  <title>AYU.OS Boot Sequence</title>
  <desc>Operating system boot sequence animation showing version and readiness status.</desc>
  <defs>
    <style>
      .ayu-surface {{ fill: #09090B; }}
      .ayu-border {{ fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }}
      .ayu-accent {{ fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }}
      .ayu-text-primary {{ fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 14px; }}
      .ayu-text-muted {{ fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; }}
      .ayu-success {{ fill: #22C55E; }}
      .ayu-boot-line {{ fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 11px; animation: typeIn 2s steps(40) forwards; opacity: 0; }}
      @keyframes typeIn {{
        0% {{ opacity: 0; }}
        100% {{ opacity: 1; }}
      }}
    </style>
  </defs>
  <rect class="ayu-surface" width="1000" height="120" rx="12"/>
  <rect class="ayu-border" width="1000" height="120" rx="12"/>
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 108 L 28 92 L 12 92"/>
    <path class="ayu-accent" d="M 972 108 L 972 92 L 988 92"/>
  </g>
  <line class="ayu-border" x1="32" y1="56" x2="968" y2="56"/>
  <text class="ayu-text-primary" x="40" y="36">BOOT SEQUENCE</text>
  <text class="ayu-text-muted" x="40" y="56">AYU.OS v{version} • {codename} • Initializing...</text>
  <circle class="ayu-success" cx="920" cy="36" r="4"/>
  <text class="ayu-text-muted" x="936" y="40">READY</text>
  <g id="ayu-boot-log" transform="translate(40, 72)">
    <text class="ayu-boot-line" x="0" y="0" style="animation-delay: 0.1s;">[OK] Kernel synchronized.</text>
    <text class="ayu-boot-line" x="0" y="18" style="animation-delay: 0.4s;">[OK] Modules loaded: {module_count} active.</text>
    <text class="ayu-boot-line" x="0" y="36" style="animation-delay: 0.7s;">[OK] AI Core initialized — Local LLM ready.</text>
    <text class="ayu-boot-line" x="0" y="54" style="animation-delay: 1.0s;">[OK] Ethereum module loaded — EIPSINSIGHT connected.</text>
    <text class="ayu-boot-line" x="0" y="72" style="animation-delay: 1.3s;">[OK] Automation engine online — Playwright + Ollama.</text>
    <text class="ayu-boot-line" x="0" y="90" style="animation-delay: 1.6s;">> System ready. Awaiting input...</text>
  </g>
</svg>"""
    
    return render_template(svg_content, {
        "VERSION": version,
        "CODENAME": codename,
        "MODULE_COUNT": str(module_count)
    })

def format_skills(skills_data: dict) -> str:
    """Format skills categories as markdown."""
    lines = []
    for category in skills_data.get("categories", []):
        lines.append(f"**{category['name']}**")
        items = [f"`{item['name']}`" for item in category.get("items", [])]
        lines.append(" ".join(items))
        lines.append("")
    return "\n".join(lines)

def format_projects(projects_data: dict) -> str:
    """Format featured projects as markdown."""
    lines = []
    for project in projects_data.get("featured", []):
        if not project.get("featured", True):
            continue
        
        lines.append(f"### {project.get('name', 'Untitled Project')}")
        lines.append(f"*{project.get('description', '')}*")
        lines.append("")
        
        # Tech stack
        tech = project.get("tech_stack", [])
        if tech:
            lines.append(f"- **Tech:** {', '.join(tech)}")
        
        # Highlights
        highlights = project.get("highlights", [])
        if highlights:
            lines.append(f"- **Highlights:**")
            for h in highlights[:3]:
                lines.append(f"  - {h}")
        
        # Repo
        repo_url = project.get("repo_url", "")
        if repo_url:
            lines.append(f"- **Repo:** [{repo_url}]({repo_url})")
        
        lines.append("")
        lines.append("---")
        lines.append("")
    
    return "\n".join(lines)

def format_experience(experience_data: dict) -> str:
    """Format experience timeline as markdown."""
    lines = []
    for pos in experience_data.get("positions", []):
        current = pos.get("current", False)
        end = "Present" if current else pos.get("end", "")
        period = f"{pos.get('start', '')} – {end}"
        
        lines.append(f"### {pos.get('role', 'Role')} at {pos.get('company', 'Company')}")
        lines.append(f"*{period} | {pos.get('location', '')}*")
        lines.append(f"{pos.get('description', '')}")
        lines.append("")
        
        achievements = pos.get("achievements", [])
        if achievements:
            lines.append("**Key Achievements:**")
            for a in achievements:
                lines.append(f"- {a}")
            lines.append("")
        
        tech = pos.get("technologies", [])
        if tech:
            lines.append(f"**Technologies:** {', '.join(tech)}")
            lines.append("")
        
        lines.append("---")
        lines.append("")
    
    return "\n".join(lines)

def format_research(research_data: dict) -> str:
    """Format research areas as markdown."""
    lines = []
    for area in research_data.get("areas", []):
        lines.append(f"### {area.get('name', 'Area')}")
        lines.append(f"{area.get('description', '')}")
        lines.append("")
        
        links = area.get("links", [])
        if links:
            link_strs = [f"[{l['label']}]({l['url']})" for l in links if l.get("url")]
            if link_strs:
                lines.append(f"Links: {' | '.join(link_strs)}")
                lines.append("")
        
        lines.append("---")
        lines.append("")
    
    return "\n".join(lines)

def format_objectives(objectives_data: dict) -> str:
    """Format current objectives as markdown."""
    lines = []
    for obj in objectives_data.get("objectives", []):
        status_emoji = {"in_progress": "🔄", "planned": "📋", "completed": "✅"}.get(obj.get("status", ""), "📋")
        lines.append(f"- {status_emoji} **{obj.get('title', 'Objective')}** ({obj.get('progress', 0)}%)")
        lines.append(f"  {obj.get('description', '')}")
        if obj.get("target_date"):
            lines.append(f"  Target: {obj['target_date']}")
        lines.append("")
    return "\n".join(lines)

def format_contact(contact_data: dict) -> str:
    """Format contact channels as markdown."""
    lines = []
    for channel in contact_data.get("channels", []):
        primary = " ★" if channel.get("primary") else ""
        lines.append(f"- **{channel['channel']}**: [{channel['handle']}]({channel['url']}){primary}")
    lines.append("")
    lines.append(f"*Preferred: {contact_data.get('preferred', 'GitHub Issues or Email')}*")
    return "\n".join(lines)


def create_github_readme(readme: str) -> None:
    """Create a GitHub-optimized README that references assets via raw.githubusercontent.com URLs."""
    # For now, the local assets work fine since we copy them to root/assets
    # This function is a placeholder for future optimization
    pass


def build_readme() -> str:
    
    # Load all data
    profile = load_json(DATA_DIR / "profile.json")
    skills = load_json(DATA_DIR / "skills.json")
    projects = load_json(DATA_DIR / "projects.json")
    experience = load_json(DATA_DIR / "experience.json")
    research = load_json(DATA_DIR / "research.json")
    objectives = load_json(DATA_DIR / "objectives.json")
    contact = load_json(DATA_DIR / "contact.json")
    stats = load_json(DATA_DIR / "stats.json")
    
    version = "7.0.0"
    codename = "AYU.OS Core"
    module_count = 8
    
    sections = []
    
    # 1. Boot Sequence
    boot_svg = render_boot_sequence(version, codename, module_count)
    sections.append(f'<div align="center">\n{boot_svg}\n</div>')
    
    # 2. Profile Header
    sections.append("---\n")
    sections.append(f"# {profile.get('name', 'Ayush N Shetty')}")
    sections.append(f"**{profile.get('title', 'Product Engineer')}** — {profile.get('subtitle', '')}")
    sections.append(f"*{profile.get('location', 'Bangalore, India')} • {profile.get('timezone', 'UTC+5:30')}*")
    sections.append("")
    sections.append(profile.get('bio', ''))
    sections.append("")
    
    # 3. Mission Control
    sections.append("---\n")
    sections.append(render_section_header("MISSION CONTROL", "Active modules and system status"))
    sections.append("")
    
    modules = [
        ("Kernel", "active", "System initialization and runtime management"),
        ("Mission Control", "active", "Active projects and career timeline"),
        ("AI Core", "active", "Reasoning engine and local LLM orchestration"),
        ("Research Database", "active", "Articles, blogs, and documentation"),
        ("Filesystem", "active", "Public repositories and subsystems"),
        ("Telemetry", "active", "GitHub statistics and system metrics"),
        ("Network", "standby", "Connections and packet routing"),
        ("Archive", "standby", "Past work and deprecated modules"),
    ]
    sections.append("| Module | Status | Description |")
    sections.append("|--------|--------|-------------|")
    for name, status, desc in modules:
        status_badge = "🟢" if status == "active" else "🟡"
        sections.append(f"| {name} | {status_badge} {status.upper()} | {desc} |")
    sections.append("")
    
    # 4. Developer Profile
    sections.append("---\n")
    sections.append(render_section_header("DEVELOPER PROFILE", "Engineering-focused summary. Not a biography."))
    sections.append("")
    sections.append("**Focus Areas:**")
    for focus in [
        "Architecting autonomous AI browser agents with local LLM orchestration",
        "Building Ethereum governance analytics & EIP diagnostics (EIPSINSIGHT)",
        "Designing developer infrastructure and systems automation",
        "Local-first AI infrastructure: distributed inference + browser automation",
        "Post-quantum cryptography research: biometric key derivation",
    ]:
        sections.append(f"- {focus}")
    sections.append("")
    
    # 5. Technology Stack
    sections.append("---\n")
    sections.append(render_section_header("TECHNOLOGY STACK", "Languages • Infrastructure • Focus Areas"))
    sections.append("")
    sections.append(format_skills(skills))
    
    # 6. Featured Projects
    sections.append("---\n")
    sections.append(render_section_header("FEATURED PROJECTS", "Deployed modules. Active repositories."))
    sections.append("")
    sections.append(format_projects(projects))
    
    # 7. Experience Timeline
    sections.append("---\n")
    sections.append(render_section_header("EXPERIENCE TIMELINE", "Career progression. Newest first."))
    sections.append("")
    sections.append(format_experience(experience))
    
    # 8. Research
    sections.append("---\n")
    sections.append(render_section_header("RESEARCH", "Current areas of interest and investigation."))
    sections.append("")
    sections.append(format_research(research))
    
    # 9. Current Objectives
    sections.append("---\n")
    sections.append(render_section_header("CURRENT OBJECTIVES", "Active missions and focus areas."))
    sections.append("")
    sections.append(format_objectives(objectives))
    
    # 10. Terminal
    sections.append("---\n")
    sections.append(render_section_header("TERMINAL", "Interactive command reference"))
    sections.append("")
    sections.append("```text")
    sections.append("$ ayu-os init")
    sections.append("[OK] Kernel synchronized.")
    sections.append("[OK] Modules loaded: 8 active.")
    sections.append("[OK] AI Core initialized — Local LLM ready.")
    sections.append("[OK] Ethereum module loaded — EIPSINSIGHT connected.")
    sections.append("[OK] Automation engine online — Playwright + Ollama.")
    sections.append("> System ready. Awaiting input...")
    sections.append("$ ")
    sections.append("```")
    sections.append("")
    
    # 11. GitHub Stats
    if stats:
        sections.append("---\n")
        sections.append(render_section_header("TELEMETRY", "GitHub statistics and system metrics"))
        sections.append("")
        sections.append(f"- **Public Repositories:** {stats.get('public_repos', '—')}")
        sections.append(f"- **Total Stars:** {stats.get('total_stars', '—')}")
        sections.append(f"- **Total Forks:** {stats.get('total_forks', '—')}")
        sections.append(f"- **Commits (1yr):** {stats.get('total_commits_1y', '—')}")
        sections.append(f"- **Followers:** {stats.get('followers', '—')}")
        sections.append(f"- **Following:** {stats.get('following', '—')}")
        sections.append(f"- **Current Streak:** {stats.get('streak_current', '—')} days")
        sections.append(f"- **Longest Streak:** {stats.get('streak_longest', '—')} days")
        if stats.get('top_languages'):
            sections.append("\n**Top Languages:**")
            for lang in stats['top_languages'][:5]:
                sections.append(f"- {lang['language']}: {lang.get('percentage', '—')}%")
        sections.append("")
    
    # 12. Contact
    sections.append("---\n")
    sections.append(render_section_header("CONTACT", "Establish connection"))
    sections.append("")
    sections.append(format_contact(contact))
    sections.append("")
    
    # Footer
    sections.append("---\n")
    sections.append(f"> {profile.get('tagline', 'Shipping real products. Exploring MPC/TSS security. Code that actually scales.')}")
    sections.append("")
    sections.append(f"Repository Version: v{version}")
    sections.append(f"Last Generated: {datetime.utcnow().isoformat()}Z")
    sections.append("")
    sections.append("[![Built with AYU.OS](https://img.shields.io/badge/Built%20with-AYU.OS-DC2626?style=flat-square)](https://github.com/AyuShetty/AyuShetty)")
    
    return "\n".join(sections)

def copy_assets():
    """Copy component SVGs to dist/assets."""
    if ASSETS_DIR.exists():
        shutil.rmtree(ASSETS_DIR)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    
    for src_dir, dst_name in [
        (COMPONENTS_DIR / "primitives", "primitives"),
        (COMPONENTS_DIR / "layouts", "layouts"),
        (COMPONENTS_DIR / "features", "features"),
    ]:
        if src_dir.exists():
            dst_dir = ASSETS_DIR / dst_name
            shutil.copytree(src_dir, dst_dir)
            print(f"  Copied {src_dir.name} → {dst_dir}")

def main():
    print("AYU.OS Build System v2.0")
    print("=" * 40)
    
    version = "7.0.0"
    
    # Create dist directory
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    
    # Build README
    print("Building README...")
    readme = build_readme()
    (DIST_DIR / "README.md").write_text(readme, encoding="utf-8")
    print(f"  ✓ Generated {DIST_DIR / 'README.md'}")
    
    # Copy assets
    print("Copying assets...")
    copy_assets()
    
    # Copy to root for GitHub profile
    shutil.copy2(DIST_DIR / "README.md", ROOT_README)
    print(f"  ✓ Updated {ROOT_README}")
    
    # Copy assets to root/assets for GitHub rendering
    if ROOT_ASSETS.exists():
        shutil.rmtree(ROOT_ASSETS)
    shutil.copytree(ASSETS_DIR, ROOT_ASSETS)
    print(f"  ✓ Synced assets to {ROOT_ASSETS}")
    
    # Also create a clean README that references assets from GitHub raw URLs
    create_github_readme(readme)
    
    print("\n✅ Build complete!")
    print(f"   Version: {version}")
    print(f"   Output: {DIST_DIR}")
    print(f"   Profile README: {ROOT_README}")

if __name__ == "__main__":
    main()