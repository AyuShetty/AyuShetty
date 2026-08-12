<div align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 120" role="img">
  <title>AYU.OS Boot Sequence</title>
  <desc>Operating system boot sequence animation showing version and readiness status.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-text-primary { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 14px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; }
      .ayu-success { fill: #22C55E; }
      .ayu-boot-line { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 11px; animation: typeIn 2s steps(40) forwards; opacity: 0; }
      @keyframes typeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
      }
    </style>
  </defs>

  <!-- Background Panel -->
  <rect class="ayu-surface" width="1000" height="120" rx="12"/>
  <rect class="ayu-border" width="1000" height="120" rx="12"/>

  <!-- Corner Accents -->
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 108 L 28 92 L 12 92"/>
    <path class="ayu-accent" d="M 972 108 L 972 92 L 988 92"/>
  </g>

  <!-- Separator -->
  <line class="ayu-border" x1="32" y1="56" x2="968" y2="56"/>

  <!-- Header -->
  <text class="ayu-text-primary" x="40" y="36">BOOT SEQUENCE</text>
  <text class="ayu-text-muted" x="40" y="56">AYU.OS v2.0.0 • AYU.OS Core • Initializing...</text>

  <!-- Status Indicator -->
  <circle class="ayu-success" cx="920" cy="36" r="4"/>
  <text class="ayu-text-muted" x="936" y="40">READY</text>

  <!-- Boot Log Lines (animated) -->
  <g id="ayu-boot-log" transform="translate(40, 72)">
    <text class="ayu-boot-line" x="0" y="0" style="animation-delay: 0.1s;">[OK] Kernel synchronized.</text>
    <text class="ayu-boot-line" x="0" y="18" style="animation-delay: 0.4s;">[OK] Modules loaded: 8 active.</text>
    <text class="ayu-boot-line" x="0" y="36" style="animation-delay: 0.7s;">[OK] AI Core initialized — Local LLM ready.</text>
    <text class="ayu-boot-line" x="0" y="54" style="animation-delay: 1.0s;">[OK] Ethereum module loaded — EIPSINSIGHT connected.</text>
    <text class="ayu-boot-line" x="0" y="72" style="animation-delay: 1.3s;">[OK] Automation engine online — Playwright + Ollama.</text>
    <text class="ayu-boot-line" x="0" y="90" style="animation-delay: 1.6s;">> System ready. Awaiting input...</text>
  </g>
</svg>
</div>
---

# Ayush N Shetty
**Product Engineer** — Autonomous AI Browser Agents · Developer Infrastructure · Ethereum Protocols · iOS & Blockchain Builder
*Bangalore, India • UTC+5:30*

iOS + blockchain builder shipping real products, exploring MPC/TSS security, hackathons, product thinking and code that actually scales. Building clean, reliable, high-performance software with an obsessive focus on detail and design refinement.

> **🚀 [Experience the Interactive Demo →](https://ayushetty.me)** — 3D dome gallery, scroll animations, bronze design system

> **🛠️ [View Source on GitHub →](https://github.com/AyuShetty/AyuShetty)** — This profile's component-driven architecture

---

<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Header Component
Purpose: Page header with title and status
Version: 2.0
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 80" role="img">
  <title>MISSION CONTROL — AYU.OS</title>
  <desc>Active modules and system status</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: Menlo, monospace; font-size: 14px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: Menlo, monospace; font-size: 10px; }
      .ayu-success { fill: #22C55E; }
    </style>
  </defs>
  <!-- Background -->
  <rect class="ayu-surface" width="1000" height="80" rx="12"/>
  <rect class="ayu-border" width="1000" height="80" rx="12"/>
  <!-- Corner Accents -->
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 68 L 28 52 L 12 52"/>
    <path class="ayu-accent" d="M 972 68 L 972 52 L 988 52"/>
  </g>
  <!-- Title -->
  <g id="ayu-title-group">
    <text class="ayu-text-primary" x="32" y="36">MISSION CONTROL</text>
    <text class="ayu-text-muted" x="32" y="56">Active modules and system status</text>
  </g>
  <!-- Status -->
  <g id="ayu-status-group">
    <circle class="ayu-success" cx="920" cy="36" r="4"/>
    <text class="ayu-text-muted" x="936" y="40">ACTIVE</text>
  </g>
  <!-- Separator -->
  <g id="ayu-separator-group">
    <line class="ayu-separator" x1="32" y1="68" x2="968" y2="68"/>
  </g>
</svg>


| Module | Status | Description |
|--------|--------|-------------|
| Kernel | 🟢 ACTIVE | System initialization and runtime management |
| Mission Control | 🟢 ACTIVE | Active projects and career timeline |
| AI Core | 🟢 ACTIVE | Reasoning engine and local LLM orchestration |
| Research Database | 🟢 ACTIVE | Articles, blogs, and documentation |
| Filesystem | 🟢 ACTIVE | Public repositories and subsystems |
| Telemetry | 🟢 ACTIVE | GitHub statistics and system metrics |
| Network | 🟡 STANDBY | Connections and packet routing |
| Archive | 🟡 STANDBY | Past work and deprecated modules |

---

<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Header Component
Purpose: Page header with title and status
Version: 2.0
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 80" role="img">
  <title>DEVELOPER PROFILE — AYU.OS</title>
  <desc>Engineering-focused summary. Not a biography.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: Menlo, monospace; font-size: 14px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: Menlo, monospace; font-size: 10px; }
      .ayu-success { fill: #22C55E; }
    </style>
  </defs>
  <!-- Background -->
  <rect class="ayu-surface" width="1000" height="80" rx="12"/>
  <rect class="ayu-border" width="1000" height="80" rx="12"/>
  <!-- Corner Accents -->
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 68 L 28 52 L 12 52"/>
    <path class="ayu-accent" d="M 972 68 L 972 52 L 988 52"/>
  </g>
  <!-- Title -->
  <g id="ayu-title-group">
    <text class="ayu-text-primary" x="32" y="36">DEVELOPER PROFILE</text>
    <text class="ayu-text-muted" x="32" y="56">Engineering-focused summary. Not a biography.</text>
  </g>
  <!-- Status -->
  <g id="ayu-status-group">
    <circle class="ayu-success" cx="920" cy="36" r="4"/>
    <text class="ayu-text-muted" x="936" y="40">ACTIVE</text>
  </g>
  <!-- Separator -->
  <g id="ayu-separator-group">
    <line class="ayu-separator" x1="32" y1="68" x2="968" y2="68"/>
  </g>
</svg>


**Focus Areas:**
- Architecting autonomous AI browser agents with local LLM orchestration
- Building Ethereum governance analytics & EIP diagnostics (EIPSINSIGHT)
- Designing developer infrastructure and systems automation
- Local-first AI infrastructure: distributed inference + browser automation
- Post-quantum cryptography research: biometric key derivation

---

<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Header Component
Purpose: Page header with title and status
Version: 2.0
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 80" role="img">
  <title>TECHNOLOGY STACK — AYU.OS</title>
  <desc>Languages • Infrastructure • Focus Areas</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: Menlo, monospace; font-size: 14px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: Menlo, monospace; font-size: 10px; }
      .ayu-success { fill: #22C55E; }
    </style>
  </defs>
  <!-- Background -->
  <rect class="ayu-surface" width="1000" height="80" rx="12"/>
  <rect class="ayu-border" width="1000" height="80" rx="12"/>
  <!-- Corner Accents -->
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 68 L 28 52 L 12 52"/>
    <path class="ayu-accent" d="M 972 68 L 972 52 L 988 52"/>
  </g>
  <!-- Title -->
  <g id="ayu-title-group">
    <text class="ayu-text-primary" x="32" y="36">TECHNOLOGY STACK</text>
    <text class="ayu-text-muted" x="32" y="56">Languages • Infrastructure • Focus Areas</text>
  </g>
  <!-- Status -->
  <g id="ayu-status-group">
    <circle class="ayu-success" cx="920" cy="36" r="4"/>
    <text class="ayu-text-muted" x="936" y="40">ACTIVE</text>
  </g>
  <!-- Separator -->
  <g id="ayu-separator-group">
    <line class="ayu-separator" x1="32" y1="68" x2="968" y2="68"/>
  </g>
</svg>


**Languages**
`TypeScript` `Python` `Solidity` `Swift` `JavaScript` `Go` `Rust` `Java` `C`

**Frontend & Interaction**
`Next.js` `React` `React Native` `iOS / SwiftUI` `Tailwind CSS` `Framer Motion` `Three.js / 3D Web` `WebGL / Shaders`

**Systems & Cloud**
`Docker` `Kubernetes` `AWS / GCP` `Linux Systems` `CI/CD (GitHub Actions)` `PostgreSQL` `Redis` `gRPC / Protocol Buffers`

**AI & Local LLMs**
`Ollama` `Playwright` `LangGraph / LangChain` `Local LLM Orchestration` `Browser Automation` `Open WebUI` `Computer Vision (OpenCV, MediaPipe)`

**Blockchain & Web3**
`Ethereum Protocol` `EIP Analysis & Tooling` `Solidity / Smart Contracts` `MPC / TSS Cryptography` `ENS / ENS-based Systems` `Foundry / Hardhat` `Governance Analytics`

**Focus Areas**
`Systems Design` `Developer Experience (DX)` `Product Engineering` `Autonomous AI Agents` `Design Systems & SVG Engineering` `IoT / Embedded (ESP32)`

---

<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Header Component
Purpose: Page header with title and status
Version: 2.0
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 80" role="img">
  <title>FEATURED PROJECTS — AYU.OS</title>
  <desc>Deployed modules. Active repositories.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: Menlo, monospace; font-size: 14px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: Menlo, monospace; font-size: 10px; }
      .ayu-success { fill: #22C55E; }
    </style>
  </defs>
  <!-- Background -->
  <rect class="ayu-surface" width="1000" height="80" rx="12"/>
  <rect class="ayu-border" width="1000" height="80" rx="12"/>
  <!-- Corner Accents -->
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 68 L 28 52 L 12 52"/>
    <path class="ayu-accent" d="M 972 68 L 972 52 L 988 52"/>
  </g>
  <!-- Title -->
  <g id="ayu-title-group">
    <text class="ayu-text-primary" x="32" y="36">FEATURED PROJECTS</text>
    <text class="ayu-text-muted" x="32" y="56">Deployed modules. Active repositories.</text>
  </g>
  <!-- Status -->
  <g id="ayu-status-group">
    <circle class="ayu-success" cx="920" cy="36" r="4"/>
    <text class="ayu-text-muted" x="936" y="40">ACTIVE</text>
  </g>
  <!-- Separator -->
  <g id="ayu-separator-group">
    <line class="ayu-separator" x1="32" y1="68" x2="968" y2="68"/>
  </g>
</svg>


<div align="center">
<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Project Card Component
Purpose: Reusable project showcase card for featured projects
Composes: panel, chip, divider
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 280" role="img">
  <title>LOCAL AI INFRASTRUCTURE — AYU.OS Project</title>
  <desc>Project card for LOCAL AI INFRASTRUCTURE: Distributed AI workflow platform using Python, Ollama, Docker, Playwright and Open WebUI for autonomous orchestration and local LLM execution across multiple systems.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-surface-raised { fill: #111111; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 11px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; }
      .ayu-text-heading { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 14px; font-weight: 600; }
      .ayu-text-label { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; font-weight: 500; }
      .ayu-success { fill: #22C55E; }
      .ayu-warning { fill: #EAB308; }
      .ayu-error { fill: #EF4444; }
      .ayu-info { fill: #38BDF8; }
      .ayu-chip-bg { fill: #1A1A1A; }
      .ayu-chip-border { fill: none; stroke: #27272A; stroke-width: 1; }
      .ayu-chip-text { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-metric-value { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 18px; font-weight: 600; }
      .ayu-metric-label { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-link { fill: #DC2626; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; text-decoration: underline; }
    </style>
  </defs>

  <rect class="ayu-surface" width="1000" height="280" rx="12"/>
  <rect class="ayu-border" width="1000" height="280" rx="12"/>

  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 268 L 28 252 L 12 252"/>
    <path class="ayu-accent" d="M 972 268 L 972 252 L 988 252"/>
  </g>

  <g id="ayu-header" transform="translate(32, 32)">
    <text class="ayu-text-heading" x="0" y="0">LOCAL AI INFRASTRUCTURE</text>
    <g transform="translate(600, -14)">
      <rect class="ayu-chip-bg" width="120" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="120" height="28" rx="6"/>
      <circle fill="#22C55E" cx="16" cy="14" r="4"/>
      <text class="ayu-chip-text" x="24" y="18">ACTIVE</text>
    </g>
    <g transform="translate(740, -14)">
      <rect class="ayu-chip-bg" width="80" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="80" height="28" rx="6"/>
      <text class="ayu-chip-text" x="40" y="18" text-anchor="middle">SOLO</text>
    </g>
    <g transform="translate(840, -14)">
      <rect class="ayu-chip-bg" width="60" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="60" height="28" rx="6"/>
      <text class="ayu-chip-text" x="30" y="18" text-anchor="middle">★ 0</text>
    </g>
  </g>

  <line class="ayu-separator" x1="32" y1="60" x2="968" y2="60"/>

  <g id="ayu-description" transform="translate(32, 72)">
    <text class="ayu-text-primary" x="0" y="0" style="font-size: 11px;">Distributed AI workflow platform using Python, Ollama, Docker, Playwright and Open WebUI for autonomous orchestration and local LLM execution across multiple systems.</text>
  </g>

  <g id="ayu-tech-stack" transform="translate(32, 110)">
    <text class="ayu-text-muted" x="0" y="0">TECH</text>
    <g id="ayu-tech-tags" transform="translate(50, -6)">
      <g transform="translate(0, 0)">
  <rect class="ayu-chip-bg" width="58" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="58" height="22" rx="4"/>
  <text class="ayu-chip-text" x="29" y="15" text-anchor="middle">Python</text>
</g>
<g transform="translate(66, 0)">
  <rect class="ayu-chip-bg" width="58" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="58" height="22" rx="4"/>
  <text class="ayu-chip-text" x="29" y="15" text-anchor="middle">Ollama</text>
</g>
<g transform="translate(132, 0)">
  <rect class="ayu-chip-bg" width="58" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="58" height="22" rx="4"/>
  <text class="ayu-chip-text" x="29" y="15" text-anchor="middle">Docker</text>
</g>
<g transform="translate(198, 0)">
  <rect class="ayu-chip-bg" width="86" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="86" height="22" rx="4"/>
  <text class="ayu-chip-text" x="43" y="15" text-anchor="middle">Playwright</text>
</g>
<g transform="translate(292, 0)">
  <rect class="ayu-chip-bg" width="86" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="86" height="22" rx="4"/>
  <text class="ayu-chip-text" x="43" y="15" text-anchor="middle">Open WebUI</text>
</g>
<g transform="translate(386, 0)">
  <rect class="ayu-chip-bg" width="86" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="86" height="22" rx="4"/>
  <text class="ayu-chip-text" x="43" y="15" text-anchor="middle">Kubernetes</text>
</g>
<g transform="translate(480, 0)">
  <rect class="ayu-chip-bg" width="79" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="79" height="22" rx="4"/>
  <text class="ayu-chip-text" x="39" y="15" text-anchor="middle">LangGraph</text>
</g>
    </g>
  </g>

  <g id="ayu-highlights" transform="translate(32, 150)">
    <text class="ayu-text-muted" x="0" y="0">HIGHLIGHTS</text>
    <g transform="translate(50, 0)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Multi-node inference with automatic load balancing</text>
</g>
<g transform="translate(50, 20)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Browser automation integrated into LLM workflows</text>
</g>
<g transform="translate(50, 40)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Open WebUI compatible — drop-in replacement for cloud APIs</text>
</g>
<g transform="translate(50, 60)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Production Docker Compose + Kubernetes manifests</text>
</g>
  </g>

  <g id="ayu-metrics" transform="translate(32, 210)">
    <line class="ayu-separator" x1="0" y1="-8" x2="936" y2="-8"/>
    <g class="ayu-metric" transform="translate(100, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">—</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">FILES</text>
</g>
<g class="ayu-metric" transform="translate(300, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">0</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STARS</text>
</g>
<g class="ayu-metric" transform="translate(500, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">MIT</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">LICENSE</text>
</g>
<g class="ayu-metric" transform="translate(700, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">2024-06</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">SINCE</text>
</g>
<g class="ayu-metric" transform="translate(900, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">ACTIVE</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STATUS</text>
</g>
  </g>

  <line class="ayu-separator" x1="32" y1="248" x2="968" y2="248"/>
  <g id="ayu-footer" transform="translate(32, 258)">
    <text class="ayu-text-muted" x="0" y="0">REPO:</text>
    <a href="https://github.com/AyuShetty/local_ai_infrastructure" target="_blank">
      <text class="ayu-link" x="50" y="0">https://github.com/AyuShetty/local_ai_infrastructure</text>
    </a>
  </g>
</svg>

</div>

---

<div align="center">
<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Project Card Component
Purpose: Reusable project showcase card for featured projects
Composes: panel, chip, divider
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 280" role="img">
  <title>AI WORKFLOW AUTOMATION — AYU.OS Project</title>
  <desc>Project card for AI WORKFLOW AUTOMATION: Automation framework integrating local AI models with browser automation and custom workflows to handle repetitive engineering tasks and document processing.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-surface-raised { fill: #111111; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 11px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; }
      .ayu-text-heading { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 14px; font-weight: 600; }
      .ayu-text-label { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; font-weight: 500; }
      .ayu-success { fill: #22C55E; }
      .ayu-warning { fill: #EAB308; }
      .ayu-error { fill: #EF4444; }
      .ayu-info { fill: #38BDF8; }
      .ayu-chip-bg { fill: #1A1A1A; }
      .ayu-chip-border { fill: none; stroke: #27272A; stroke-width: 1; }
      .ayu-chip-text { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-metric-value { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 18px; font-weight: 600; }
      .ayu-metric-label { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-link { fill: #DC2626; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; text-decoration: underline; }
    </style>
  </defs>

  <rect class="ayu-surface" width="1000" height="280" rx="12"/>
  <rect class="ayu-border" width="1000" height="280" rx="12"/>

  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 268 L 28 252 L 12 252"/>
    <path class="ayu-accent" d="M 972 268 L 972 252 L 988 252"/>
  </g>

  <g id="ayu-header" transform="translate(32, 32)">
    <text class="ayu-text-heading" x="0" y="0">AI WORKFLOW AUTOMATION</text>
    <g transform="translate(600, -14)">
      <rect class="ayu-chip-bg" width="120" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="120" height="28" rx="6"/>
      <circle fill="#22C55E" cx="16" cy="14" r="4"/>
      <text class="ayu-chip-text" x="24" y="18">ACTIVE</text>
    </g>
    <g transform="translate(740, -14)">
      <rect class="ayu-chip-bg" width="80" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="80" height="28" rx="6"/>
      <text class="ayu-chip-text" x="40" y="18" text-anchor="middle">SOLO</text>
    </g>
    <g transform="translate(840, -14)">
      <rect class="ayu-chip-bg" width="60" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="60" height="28" rx="6"/>
      <text class="ayu-chip-text" x="30" y="18" text-anchor="middle">★ 0</text>
    </g>
  </g>

  <line class="ayu-separator" x1="32" y1="60" x2="968" y2="60"/>

  <g id="ayu-description" transform="translate(32, 72)">
    <text class="ayu-text-primary" x="0" y="0" style="font-size: 11px;">Automation framework integrating local AI models with browser automation and custom workflows to handle repetitive engineering tasks and document processing.</text>
  </g>

  <g id="ayu-tech-stack" transform="translate(32, 110)">
    <text class="ayu-text-muted" x="0" y="0">TECH</text>
    <g id="ayu-tech-tags" transform="translate(50, -6)">
      <g transform="translate(0, 0)">
  <rect class="ayu-chip-bg" width="58" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="58" height="22" rx="4"/>
  <text class="ayu-chip-text" x="29" y="15" text-anchor="middle">Python</text>
</g>
<g transform="translate(66, 0)">
  <rect class="ayu-chip-bg" width="86" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="86" height="22" rx="4"/>
  <text class="ayu-chip-text" x="43" y="15" text-anchor="middle">Playwright</text>
</g>
<g transform="translate(160, 0)">
  <rect class="ayu-chip-bg" width="58" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="58" height="22" rx="4"/>
  <text class="ayu-chip-text" x="29" y="15" text-anchor="middle">Ollama</text>
</g>
<g transform="translate(226, 0)">
  <rect class="ayu-chip-bg" width="79" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="79" height="22" rx="4"/>
  <text class="ayu-chip-text" x="39" y="15" text-anchor="middle">LangGraph</text>
</g>
<g transform="translate(313, 0)">
  <rect class="ayu-chip-bg" width="72" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="72" height="22" rx="4"/>
  <text class="ayu-chip-text" x="36" y="15" text-anchor="middle">Pydantic</text>
</g>
<g transform="translate(393, 0)">
  <rect class="ayu-chip-bg" width="44" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="44" height="22" rx="4"/>
  <text class="ayu-chip-text" x="22" y="15" text-anchor="middle">YAML</text>
</g>
    </g>
  </g>

  <g id="ayu-highlights" transform="translate(32, 150)">
    <text class="ayu-text-muted" x="0" y="0">HIGHLIGHTS</text>
    <g transform="translate(50, 0)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">95%+ success rate on benchmark automation tasks</text>
</g>
<g transform="translate(50, 20)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Self-healing selector strategy (DOM + visual + LLM)</text>
</g>
<g transform="translate(50, 40)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">YAML workflow DSL — no code for common patterns</text>
</g>
<g transform="translate(50, 60)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Full audit trail with screenshots + reasoning logs</text>
</g>
  </g>

  <g id="ayu-metrics" transform="translate(32, 210)">
    <line class="ayu-separator" x1="0" y1="-8" x2="936" y2="-8"/>
    <g class="ayu-metric" transform="translate(100, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">—</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">FILES</text>
</g>
<g class="ayu-metric" transform="translate(300, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">0</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STARS</text>
</g>
<g class="ayu-metric" transform="translate(500, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">MIT</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">LICENSE</text>
</g>
<g class="ayu-metric" transform="translate(700, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">2024-03</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">SINCE</text>
</g>
<g class="ayu-metric" transform="translate(900, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">ACTIVE</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STATUS</text>
</g>
  </g>

  <line class="ayu-separator" x1="32" y1="248" x2="968" y2="248"/>
  <g id="ayu-footer" transform="translate(32, 258)">
    <text class="ayu-text-muted" x="0" y="0">REPO:</text>
    <a href="https://github.com/AyuShetty/ai_workflow_automation" target="_blank">
      <text class="ayu-link" x="50" y="0">https://github.com/AyuShetty/ai_workflow_automation</text>
    </a>
  </g>
</svg>

</div>

---

<div align="center">
<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Project Card Component
Purpose: Reusable project showcase card for featured projects
Composes: panel, chip, divider
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 280" role="img">
  <title>ETH.ED — AI-Powered Web3 Learning Platform — AYU.OS Project</title>
  <desc>Project card for ETH.ED — AI-Powered Web3 Learning Platform: AI-powered Web3 learning platform with gamified lessons, ENS-based certificates, and smart contract micropayments. Next.js + AI + Ethereum.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-surface-raised { fill: #111111; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 11px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; }
      .ayu-text-heading { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 14px; font-weight: 600; }
      .ayu-text-label { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; font-weight: 500; }
      .ayu-success { fill: #22C55E; }
      .ayu-warning { fill: #EAB308; }
      .ayu-error { fill: #EF4444; }
      .ayu-info { fill: #38BDF8; }
      .ayu-chip-bg { fill: #1A1A1A; }
      .ayu-chip-border { fill: none; stroke: #27272A; stroke-width: 1; }
      .ayu-chip-text { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-metric-value { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 18px; font-weight: 600; }
      .ayu-metric-label { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-link { fill: #DC2626; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; text-decoration: underline; }
    </style>
  </defs>

  <rect class="ayu-surface" width="1000" height="280" rx="12"/>
  <rect class="ayu-border" width="1000" height="280" rx="12"/>

  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 268 L 28 252 L 12 252"/>
    <path class="ayu-accent" d="M 972 268 L 972 252 L 988 252"/>
  </g>

  <g id="ayu-header" transform="translate(32, 32)">
    <text class="ayu-text-heading" x="0" y="0">ETH.ED — AI-Powered Web3 Learning Platform</text>
    <g transform="translate(600, -14)">
      <rect class="ayu-chip-bg" width="120" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="120" height="28" rx="6"/>
      <circle fill="#22C55E" cx="16" cy="14" r="4"/>
      <text class="ayu-chip-text" x="24" y="18">ACTIVE</text>
    </g>
    <g transform="translate(740, -14)">
      <rect class="ayu-chip-bg" width="80" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="80" height="28" rx="6"/>
      <text class="ayu-chip-text" x="40" y="18" text-anchor="middle">SOLO</text>
    </g>
    <g transform="translate(840, -14)">
      <rect class="ayu-chip-bg" width="60" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="60" height="28" rx="6"/>
      <text class="ayu-chip-text" x="30" y="18" text-anchor="middle">★ 1</text>
    </g>
  </g>

  <line class="ayu-separator" x1="32" y1="60" x2="968" y2="60"/>

  <g id="ayu-description" transform="translate(32, 72)">
    <text class="ayu-text-primary" x="0" y="0" style="font-size: 11px;">AI-powered Web3 learning platform with gamified lessons, ENS-based certificates, and smart contract micropayments. Next.js + AI + Ethereum.</text>
  </g>

  <g id="ayu-tech-stack" transform="translate(32, 110)">
    <text class="ayu-text-muted" x="0" y="0">TECH</text>
    <g id="ayu-tech-tags" transform="translate(50, -6)">
      <g transform="translate(0, 0)">
  <rect class="ayu-chip-bg" width="65" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="65" height="22" rx="4"/>
  <text class="ayu-chip-text" x="32" y="15" text-anchor="middle">Next.js</text>
</g>
<g transform="translate(73, 0)">
  <rect class="ayu-chip-bg" width="86" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="86" height="22" rx="4"/>
  <text class="ayu-chip-text" x="43" y="15" text-anchor="middle">TypeScript</text>
</g>
<g transform="translate(167, 0)">
  <rect class="ayu-chip-bg" width="30" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="30" height="22" rx="4"/>
  <text class="ayu-chip-text" x="15" y="15" text-anchor="middle">AI</text>
</g>
<g transform="translate(205, 0)">
  <rect class="ayu-chip-bg" width="72" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="72" height="22" rx="4"/>
  <text class="ayu-chip-text" x="36" y="15" text-anchor="middle">Ethereum</text>
</g>
<g transform="translate(285, 0)">
  <rect class="ayu-chip-bg" width="37" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="37" height="22" rx="4"/>
  <text class="ayu-chip-text" x="18" y="15" text-anchor="middle">ENS</text>
</g>
<g transform="translate(330, 0)">
  <rect class="ayu-chip-bg" width="121" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="121" height="22" rx="4"/>
  <text class="ayu-chip-text" x="60" y="15" text-anchor="middle">Smart Contracts</text>
</g>
<g transform="translate(459, 0)">
  <rect class="ayu-chip-bg" width="100" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="100" height="22" rx="4"/>
  <text class="ayu-chip-text" x="50" y="15" text-anchor="middle">Tailwind CSS</text>
</g>
    </g>
  </g>

  <g id="ayu-highlights" transform="translate(32, 150)">
    <text class="ayu-text-muted" x="0" y="0">HIGHLIGHTS</text>
    <g transform="translate(50, 0)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">ENS-based verifiable certificates (Soulbound NFTs)</text>
</g>
<g transform="translate(50, 20)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">AI tutor with RAG over Ethereum documentation</text>
</g>
<g transform="translate(50, 40)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Smart contract micropayments for content creators</text>
</g>
<g transform="translate(50, 60)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Gamified progression with on-chain reputation</text>
</g>
  </g>

  <g id="ayu-metrics" transform="translate(32, 210)">
    <line class="ayu-separator" x1="0" y1="-8" x2="936" y2="-8"/>
    <g class="ayu-metric" transform="translate(100, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">—</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">FILES</text>
</g>
<g class="ayu-metric" transform="translate(300, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">1</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STARS</text>
</g>
<g class="ayu-metric" transform="translate(500, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">MIT</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">LICENSE</text>
</g>
<g class="ayu-metric" transform="translate(700, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">2024-01</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">SINCE</text>
</g>
<g class="ayu-metric" transform="translate(900, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">ACTIVE</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STATUS</text>
</g>
  </g>

  <line class="ayu-separator" x1="32" y1="248" x2="968" y2="248"/>
  <g id="ayu-footer" transform="translate(32, 258)">
    <text class="ayu-text-muted" x="0" y="0">REPO:</text>
    <a href="https://github.com/AyuShetty/ethed-frontend" target="_blank">
      <text class="ayu-link" x="50" y="0">https://github.com/AyuShetty/ethed-frontend</text>
    </a>
  </g>
</svg>

</div>

---

<div align="center">
<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Project Card Component
Purpose: Reusable project showcase card for featured projects
Composes: panel, chip, divider
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 280" role="img">
  <title>EIPSINSIGHT — Ethereum Governance Analytics — AYU.OS Project</title>
  <desc>Project card for EIPSINSIGHT — Ethereum Governance Analytics: Ethereum governance analytics platform for tracking EIP lifecycles, governance signals, and stakeholder influence. Real-time dashboard with on-chain + off-chain data fusion.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-surface-raised { fill: #111111; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 11px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; }
      .ayu-text-heading { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 14px; font-weight: 600; }
      .ayu-text-label { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; font-weight: 500; }
      .ayu-success { fill: #22C55E; }
      .ayu-warning { fill: #EAB308; }
      .ayu-error { fill: #EF4444; }
      .ayu-info { fill: #38BDF8; }
      .ayu-chip-bg { fill: #1A1A1A; }
      .ayu-chip-border { fill: none; stroke: #27272A; stroke-width: 1; }
      .ayu-chip-text { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-metric-value { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 18px; font-weight: 600; }
      .ayu-metric-label { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-link { fill: #DC2626; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; text-decoration: underline; }
    </style>
  </defs>

  <rect class="ayu-surface" width="1000" height="280" rx="12"/>
  <rect class="ayu-border" width="1000" height="280" rx="12"/>

  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 268 L 28 252 L 12 252"/>
    <path class="ayu-accent" d="M 972 268 L 972 252 L 988 252"/>
  </g>

  <g id="ayu-header" transform="translate(32, 32)">
    <text class="ayu-text-heading" x="0" y="0">EIPSINSIGHT — Ethereum Governance Analytics</text>
    <g transform="translate(600, -14)">
      <rect class="ayu-chip-bg" width="120" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="120" height="28" rx="6"/>
      <circle fill="#22C55E" cx="16" cy="14" r="4"/>
      <text class="ayu-chip-text" x="24" y="18">ACTIVE</text>
    </g>
    <g transform="translate(740, -14)">
      <rect class="ayu-chip-bg" width="80" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="80" height="28" rx="6"/>
      <text class="ayu-chip-text" x="40" y="18" text-anchor="middle">TEAM</text>
    </g>
    <g transform="translate(840, -14)">
      <rect class="ayu-chip-bg" width="60" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="60" height="28" rx="6"/>
      <text class="ayu-chip-text" x="30" y="18" text-anchor="middle">★ 0</text>
    </g>
  </g>

  <line class="ayu-separator" x1="32" y1="60" x2="968" y2="60"/>

  <g id="ayu-description" transform="translate(32, 72)">
    <text class="ayu-text-primary" x="0" y="0" style="font-size: 11px;">Ethereum governance analytics platform for tracking EIP lifecycles, governance signals, and stakeholder influence. Real-time dashboard with on-chain + off-chain data fusion.</text>
  </g>

  <g id="ayu-tech-stack" transform="translate(32, 110)">
    <text class="ayu-text-muted" x="0" y="0">TECH</text>
    <g id="ayu-tech-tags" transform="translate(50, -6)">
      <g transform="translate(0, 0)">
  <rect class="ayu-chip-bg" width="86" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="86" height="22" rx="4"/>
  <text class="ayu-chip-text" x="43" y="15" text-anchor="middle">TypeScript</text>
</g>
<g transform="translate(94, 0)">
  <rect class="ayu-chip-bg" width="65" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="65" height="22" rx="4"/>
  <text class="ayu-chip-text" x="32" y="15" text-anchor="middle">Next.js</text>
</g>
<g transform="translate(167, 0)">
  <rect class="ayu-chip-bg" width="51" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="51" height="22" rx="4"/>
  <text class="ayu-chip-text" x="25" y="15" text-anchor="middle">React</text>
</g>
<g transform="translate(226, 0)">
  <rect class="ayu-chip-bg" width="72" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="72" height="22" rx="4"/>
  <text class="ayu-chip-text" x="36" y="15" text-anchor="middle">Ethereum</text>
</g>
<g transform="translate(306, 0)">
  <rect class="ayu-chip-bg" width="79" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="79" height="22" rx="4"/>
  <text class="ayu-chip-text" x="39" y="15" text-anchor="middle">The Graph</text>
</g>
<g transform="translate(393, 0)">
  <rect class="ayu-chip-bg" width="86" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="86" height="22" rx="4"/>
  <text class="ayu-chip-text" x="43" y="15" text-anchor="middle">PostgreSQL</text>
</g>
<g transform="translate(487, 0)">
  <rect class="ayu-chip-bg" width="86" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="86" height="22" rx="4"/>
  <text class="ayu-chip-text" x="43" y="15" text-anchor="middle">GitHub API</text>
</g>
<g transform="translate(581, 0)">
  <rect class="ayu-chip-bg" width="93" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="93" height="22" rx="4"/>
  <text class="ayu-chip-text" x="46" y="15" text-anchor="middle">Discord API</text>
</g>
    </g>
  </g>

  <g id="ayu-highlights" transform="translate(32, 150)">
    <text class="ayu-text-muted" x="0" y="0">HIGHLIGHTS</text>
    <g transform="translate(50, 0)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Tracks 200+ EIPs across lifecycle stages</text>
</g>
<g transform="translate(50, 20)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Stakeholder influence mapping (on-chain + off-chain)</text>
</g>
<g transform="translate(50, 40)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Real-time governance signal aggregation</text>
</g>
<g transform="translate(50, 60)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Predictive EIP acceptance probability model</text>
</g>
  </g>

  <g id="ayu-metrics" transform="translate(32, 210)">
    <line class="ayu-separator" x1="0" y1="-8" x2="936" y2="-8"/>
    <g class="ayu-metric" transform="translate(100, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">—</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">FILES</text>
</g>
<g class="ayu-metric" transform="translate(300, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">0</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STARS</text>
</g>
<g class="ayu-metric" transform="translate(500, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">MIT</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">LICENSE</text>
</g>
<g class="ayu-metric" transform="translate(700, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">2023-01</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">SINCE</text>
</g>
<g class="ayu-metric" transform="translate(900, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">ACTIVE</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STATUS</text>
</g>
  </g>

  <line class="ayu-separator" x1="32" y1="248" x2="968" y2="248"/>
  <g id="ayu-footer" transform="translate(32, 258)">
    <text class="ayu-text-muted" x="0" y="0">REPO:</text>
    <a href="https://github.com/AvarchLLC/EIPsInsight" target="_blank">
      <text class="ayu-link" x="50" y="0">https://github.com/AvarchLLC/EIPsInsight</text>
    </a>
  </g>
</svg>

</div>

---

<div align="center">
<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Project Card Component
Purpose: Reusable project showcase card for featured projects
Composes: panel, chip, divider
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 280" role="img">
  <title>FACIAL KEYGEN — Biometric Cryptographic Key Derivation — AYU.OS Project</title>
  <desc>Project card for FACIAL KEYGEN — Biometric Cryptographic Key Derivation: Python-based biometric authentication system generating cryptographic keys from facial biometrics using computer vision and ML for post-quantum security research.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-surface-raised { fill: #111111; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 11px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; }
      .ayu-text-heading { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 14px; font-weight: 600; }
      .ayu-text-label { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; font-weight: 500; }
      .ayu-success { fill: #22C55E; }
      .ayu-warning { fill: #EAB308; }
      .ayu-error { fill: #EF4444; }
      .ayu-info { fill: #38BDF8; }
      .ayu-chip-bg { fill: #1A1A1A; }
      .ayu-chip-border { fill: none; stroke: #27272A; stroke-width: 1; }
      .ayu-chip-text { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-metric-value { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 18px; font-weight: 600; }
      .ayu-metric-label { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-link { fill: #DC2626; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; text-decoration: underline; }
    </style>
  </defs>

  <rect class="ayu-surface" width="1000" height="280" rx="12"/>
  <rect class="ayu-border" width="1000" height="280" rx="12"/>

  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 268 L 28 252 L 12 252"/>
    <path class="ayu-accent" d="M 972 268 L 972 252 L 988 252"/>
  </g>

  <g id="ayu-header" transform="translate(32, 32)">
    <text class="ayu-text-heading" x="0" y="0">FACIAL KEYGEN — Biometric Cryptographic Key Derivation</text>
    <g transform="translate(600, -14)">
      <rect class="ayu-chip-bg" width="120" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="120" height="28" rx="6"/>
      <circle fill="#22C55E" cx="16" cy="14" r="4"/>
      <text class="ayu-chip-text" x="24" y="18">ACTIVE</text>
    </g>
    <g transform="translate(740, -14)">
      <rect class="ayu-chip-bg" width="80" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="80" height="28" rx="6"/>
      <text class="ayu-chip-text" x="40" y="18" text-anchor="middle">SOLO</text>
    </g>
    <g transform="translate(840, -14)">
      <rect class="ayu-chip-bg" width="60" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="60" height="28" rx="6"/>
      <text class="ayu-chip-text" x="30" y="18" text-anchor="middle">★ 0</text>
    </g>
  </g>

  <line class="ayu-separator" x1="32" y1="60" x2="968" y2="60"/>

  <g id="ayu-description" transform="translate(32, 72)">
    <text class="ayu-text-primary" x="0" y="0" style="font-size: 11px;">Python-based biometric authentication system generating cryptographic keys from facial biometrics using computer vision and ML for post-quantum security research.</text>
  </g>

  <g id="ayu-tech-stack" transform="translate(32, 110)">
    <text class="ayu-text-muted" x="0" y="0">TECH</text>
    <g id="ayu-tech-tags" transform="translate(50, -6)">
      <g transform="translate(0, 0)">
  <rect class="ayu-chip-bg" width="58" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="58" height="22" rx="4"/>
  <text class="ayu-chip-text" x="29" y="15" text-anchor="middle">Python</text>
</g>
<g transform="translate(66, 0)">
  <rect class="ayu-chip-bg" width="58" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="58" height="22" rx="4"/>
  <text class="ayu-chip-text" x="29" y="15" text-anchor="middle">OpenCV</text>
</g>
<g transform="translate(132, 0)">
  <rect class="ayu-chip-bg" width="79" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="79" height="22" rx="4"/>
  <text class="ayu-chip-text" x="39" y="15" text-anchor="middle">MediaPipe</text>
</g>
<g transform="translate(219, 0)">
  <rect class="ayu-chip-bg" width="65" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="65" height="22" rx="4"/>
  <text class="ayu-chip-text" x="32" y="15" text-anchor="middle">PyTorch</text>
</g>
<g transform="translate(292, 0)">
  <rect class="ayu-chip-bg" width="100" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="100" height="22" rx="4"/>
  <text class="ayu-chip-text" x="50" y="15" text-anchor="middle">Cryptography</text>
</g>
<g transform="translate(400, 0)">
  <rect class="ayu-chip-bg" width="51" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="51" height="22" rx="4"/>
  <text class="ayu-chip-text" x="25" y="15" text-anchor="middle">NumPy</text>
</g>
    </g>
  </g>

  <g id="ayu-highlights" transform="translate(32, 150)">
    <text class="ayu-text-muted" x="0" y="0">HIGHLIGHTS</text>
    <g transform="translate(50, 0)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Novel biometric-to-crypto key derivation pipeline</text>
</g>
<g transform="translate(50, 20)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Post-quantum secure key derivation (CRYSTALS-Dilithium compatible)</text>
</g>
<g transform="translate(50, 40)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Fuzzy extractor with >99% reproduction rate</text>
</g>
<g transform="translate(50, 60)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Open-source reference implementation with tests</text>
</g>
  </g>

  <g id="ayu-metrics" transform="translate(32, 210)">
    <line class="ayu-separator" x1="0" y1="-8" x2="936" y2="-8"/>
    <g class="ayu-metric" transform="translate(100, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">—</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">FILES</text>
</g>
<g class="ayu-metric" transform="translate(300, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">0</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STARS</text>
</g>
<g class="ayu-metric" transform="translate(500, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">MIT</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">LICENSE</text>
</g>
<g class="ayu-metric" transform="translate(700, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">2025-02</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">SINCE</text>
</g>
<g class="ayu-metric" transform="translate(900, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">ACTIVE</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STATUS</text>
</g>
  </g>

  <line class="ayu-separator" x1="32" y1="248" x2="968" y2="248"/>
  <g id="ayu-footer" transform="translate(32, 258)">
    <text class="ayu-text-muted" x="0" y="0">REPO:</text>
    <a href="https://github.com/AyuShetty/facial_keygen" target="_blank">
      <text class="ayu-link" x="50" y="0">https://github.com/AyuShetty/facial_keygen</text>
    </a>
  </g>
</svg>

</div>

---

<div align="center">
<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Project Card Component
Purpose: Reusable project showcase card for featured projects
Composes: panel, chip, divider
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 280" role="img">
  <title>AIRGESTURE — Touchless Presentation Control — AYU.OS Project</title>
  <desc>Project card for AIRGESTURE — Touchless Presentation Control: Real-time computer vision app using OpenCV and MediaPipe that translates hand gestures into presentation controls for touchless classroom interaction.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-surface-raised { fill: #111111; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 11px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; }
      .ayu-text-heading { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 14px; font-weight: 600; }
      .ayu-text-label { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; font-weight: 500; }
      .ayu-success { fill: #22C55E; }
      .ayu-warning { fill: #EAB308; }
      .ayu-error { fill: #EF4444; }
      .ayu-info { fill: #38BDF8; }
      .ayu-chip-bg { fill: #1A1A1A; }
      .ayu-chip-border { fill: none; stroke: #27272A; stroke-width: 1; }
      .ayu-chip-text { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-metric-value { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 18px; font-weight: 600; }
      .ayu-metric-label { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-link { fill: #DC2626; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; text-decoration: underline; }
    </style>
  </defs>

  <rect class="ayu-surface" width="1000" height="280" rx="12"/>
  <rect class="ayu-border" width="1000" height="280" rx="12"/>

  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 268 L 28 252 L 12 252"/>
    <path class="ayu-accent" d="M 972 268 L 972 252 L 988 252"/>
  </g>

  <g id="ayu-header" transform="translate(32, 32)">
    <text class="ayu-text-heading" x="0" y="0">AIRGESTURE — Touchless Presentation Control</text>
    <g transform="translate(600, -14)">
      <rect class="ayu-chip-bg" width="120" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="120" height="28" rx="6"/>
      <circle fill="#22C55E" cx="16" cy="14" r="4"/>
      <text class="ayu-chip-text" x="24" y="18">ACTIVE</text>
    </g>
    <g transform="translate(740, -14)">
      <rect class="ayu-chip-bg" width="80" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="80" height="28" rx="6"/>
      <text class="ayu-chip-text" x="40" y="18" text-anchor="middle">SOLO</text>
    </g>
    <g transform="translate(840, -14)">
      <rect class="ayu-chip-bg" width="60" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="60" height="28" rx="6"/>
      <text class="ayu-chip-text" x="30" y="18" text-anchor="middle">★ 1</text>
    </g>
  </g>

  <line class="ayu-separator" x1="32" y1="60" x2="968" y2="60"/>

  <g id="ayu-description" transform="translate(32, 72)">
    <text class="ayu-text-primary" x="0" y="0" style="font-size: 11px;">Real-time computer vision app using OpenCV and MediaPipe that translates hand gestures into presentation controls for touchless classroom interaction.</text>
  </g>

  <g id="ayu-tech-stack" transform="translate(32, 110)">
    <text class="ayu-text-muted" x="0" y="0">TECH</text>
    <g id="ayu-tech-tags" transform="translate(50, -6)">
      <g transform="translate(0, 0)">
  <rect class="ayu-chip-bg" width="58" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="58" height="22" rx="4"/>
  <text class="ayu-chip-text" x="29" y="15" text-anchor="middle">Python</text>
</g>
<g transform="translate(66, 0)">
  <rect class="ayu-chip-bg" width="58" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="58" height="22" rx="4"/>
  <text class="ayu-chip-text" x="29" y="15" text-anchor="middle">OpenCV</text>
</g>
<g transform="translate(132, 0)">
  <rect class="ayu-chip-bg" width="79" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="79" height="22" rx="4"/>
  <text class="ayu-chip-text" x="39" y="15" text-anchor="middle">MediaPipe</text>
</g>
<g transform="translate(219, 0)">
  <rect class="ayu-chip-bg" width="79" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="79" height="22" rx="4"/>
  <text class="ayu-chip-text" x="39" y="15" text-anchor="middle">PyAutoGUI</text>
</g>
<g transform="translate(306, 0)">
  <rect class="ayu-chip-bg" width="51" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="51" height="22" rx="4"/>
  <text class="ayu-chip-text" x="25" y="15" text-anchor="middle">NumPy</text>
</g>
    </g>
  </g>

  <g id="ayu-highlights" transform="translate(32, 150)">
    <text class="ayu-text-muted" x="0" y="0">HIGHLIGHTS</text>
    <g transform="translate(50, 0)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Sub-50ms gesture-to-action latency</text>
</g>
<g transform="translate(50, 20)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">8 gesture classes with 95%+ accuracy</text>
</g>
<g transform="translate(50, 40)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Zero external dependencies — runs fully offline</text>
</g>
<g transform="translate(50, 60)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Accessibility-focused: configurable sensitivity</text>
</g>
  </g>

  <g id="ayu-metrics" transform="translate(32, 210)">
    <line class="ayu-separator" x1="0" y1="-8" x2="936" y2="-8"/>
    <g class="ayu-metric" transform="translate(100, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">—</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">FILES</text>
</g>
<g class="ayu-metric" transform="translate(300, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">1</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STARS</text>
</g>
<g class="ayu-metric" transform="translate(500, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">MIT</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">LICENSE</text>
</g>
<g class="ayu-metric" transform="translate(700, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">2025-01</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">SINCE</text>
</g>
<g class="ayu-metric" transform="translate(900, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">ACTIVE</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STATUS</text>
</g>
  </g>

  <line class="ayu-separator" x1="32" y1="248" x2="968" y2="248"/>
  <g id="ayu-footer" transform="translate(32, 258)">
    <text class="ayu-text-muted" x="0" y="0">REPO:</text>
    <a href="https://github.com/AyuShetty/airgesture" target="_blank">
      <text class="ayu-link" x="50" y="0">https://github.com/AyuShetty/airgesture</text>
    </a>
  </g>
</svg>

</div>

---

<div align="center">
<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Project Card Component
Purpose: Reusable project showcase card for featured projects
Composes: panel, chip, divider
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 280" role="img">
  <title>ETHERWORLD IOS — Scalable iOS App Architecture — AYU.OS Project</title>
  <desc>Project card for ETHERWORLD IOS — Scalable iOS App Architecture: Designed the application architecture and modular structure for the EtherWorld iOS app — scalable navigation, API integration, and maintainable app structure.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-surface-raised { fill: #111111; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 11px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; }
      .ayu-text-heading { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 14px; font-weight: 600; }
      .ayu-text-label { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; font-weight: 500; }
      .ayu-success { fill: #22C55E; }
      .ayu-warning { fill: #EAB308; }
      .ayu-error { fill: #EF4444; }
      .ayu-info { fill: #38BDF8; }
      .ayu-chip-bg { fill: #1A1A1A; }
      .ayu-chip-border { fill: none; stroke: #27272A; stroke-width: 1; }
      .ayu-chip-text { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-metric-value { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 18px; font-weight: 600; }
      .ayu-metric-label { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-link { fill: #DC2626; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; text-decoration: underline; }
    </style>
  </defs>

  <rect class="ayu-surface" width="1000" height="280" rx="12"/>
  <rect class="ayu-border" width="1000" height="280" rx="12"/>

  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 268 L 28 252 L 12 252"/>
    <path class="ayu-accent" d="M 972 268 L 972 252 L 988 252"/>
  </g>

  <g id="ayu-header" transform="translate(32, 32)">
    <text class="ayu-text-heading" x="0" y="0">ETHERWORLD IOS — Scalable iOS App Architecture</text>
    <g transform="translate(600, -14)">
      <rect class="ayu-chip-bg" width="120" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="120" height="28" rx="6"/>
      <circle fill="#22C55E" cx="16" cy="14" r="4"/>
      <text class="ayu-chip-text" x="24" y="18">ACTIVE</text>
    </g>
    <g transform="translate(740, -14)">
      <rect class="ayu-chip-bg" width="80" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="80" height="28" rx="6"/>
      <text class="ayu-chip-text" x="40" y="18" text-anchor="middle">SOLO</text>
    </g>
    <g transform="translate(840, -14)">
      <rect class="ayu-chip-bg" width="60" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="60" height="28" rx="6"/>
      <text class="ayu-chip-text" x="30" y="18" text-anchor="middle">★ 0</text>
    </g>
  </g>

  <line class="ayu-separator" x1="32" y1="60" x2="968" y2="60"/>

  <g id="ayu-description" transform="translate(32, 72)">
    <text class="ayu-text-primary" x="0" y="0" style="font-size: 11px;">Designed the application architecture and modular structure for the EtherWorld iOS app — scalable navigation, API integration, and maintainable app structure.</text>
  </g>

  <g id="ayu-tech-stack" transform="translate(32, 110)">
    <text class="ayu-text-muted" x="0" y="0">TECH</text>
    <g id="ayu-tech-tags" transform="translate(50, -6)">
      <g transform="translate(0, 0)">
  <rect class="ayu-chip-bg" width="51" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="51" height="22" rx="4"/>
  <text class="ayu-chip-text" x="25" y="15" text-anchor="middle">Swift</text>
</g>
<g transform="translate(59, 0)">
  <rect class="ayu-chip-bg" width="65" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="65" height="22" rx="4"/>
  <text class="ayu-chip-text" x="32" y="15" text-anchor="middle">SwiftUI</text>
</g>
<g transform="translate(132, 0)">
  <rect class="ayu-chip-bg" width="65" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="65" height="22" rx="4"/>
  <text class="ayu-chip-text" x="32" y="15" text-anchor="middle">Combine</text>
</g>
<g transform="translate(205, 0)">
  <rect class="ayu-chip-bg" width="86" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="86" height="22" rx="4"/>
  <text class="ayu-chip-text" x="43" y="15" text-anchor="middle">Web3.swift</text>
</g>
<g transform="translate(299, 0)">
  <rect class="ayu-chip-bg" width="58" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="58" height="22" rx="4"/>
  <text class="ayu-chip-text" x="29" y="15" text-anchor="middle">XCTest</text>
</g>
<g transform="translate(365, 0)">
  <rect class="ayu-chip-bg" width="72" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="72" height="22" rx="4"/>
  <text class="ayu-chip-text" x="36" y="15" text-anchor="middle">Fastlane</text>
</g>
    </g>
  </g>

  <g id="ayu-highlights" transform="translate(32, 150)">
    <text class="ayu-text-muted" x="0" y="0">HIGHLIGHTS</text>
    <g transform="translate(50, 0)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Zero-massive-view-controller architecture</text>
</g>
<g transform="translate(50, 20)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Type-safe API layer with code generation</text>
</g>
<g transform="translate(50, 40)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Web3 transaction signing flow with Secure Enclave</text>
</g>
<g transform="translate(50, 60)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Feature-flag driven development</text>
</g>
  </g>

  <g id="ayu-metrics" transform="translate(32, 210)">
    <line class="ayu-separator" x1="0" y1="-8" x2="936" y2="-8"/>
    <g class="ayu-metric" transform="translate(100, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">—</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">FILES</text>
</g>
<g class="ayu-metric" transform="translate(300, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">0</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STARS</text>
</g>
<g class="ayu-metric" transform="translate(500, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">MIT</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">LICENSE</text>
</g>
<g class="ayu-metric" transform="translate(700, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">2025-04</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">SINCE</text>
</g>
<g class="ayu-metric" transform="translate(900, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">ACTIVE</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STATUS</text>
</g>
  </g>

  <line class="ayu-separator" x1="32" y1="248" x2="968" y2="248"/>
  <g id="ayu-footer" transform="translate(32, 258)">
    <text class="ayu-text-muted" x="0" y="0">REPO:</text>
    <a href="https://github.com/AyuShetty/etherworld_ios" target="_blank">
      <text class="ayu-link" x="50" y="0">https://github.com/AyuShetty/etherworld_ios</text>
    </a>
  </g>
</svg>

</div>

---

<div align="center">
<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Project Card Component
Purpose: Reusable project showcase card for featured projects
Composes: panel, chip, divider
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 280" role="img">
  <title>THIS PORTFOLIO — Immersive 3D Developer Portfolio — AYU.OS Project</title>
  <desc>Project card for THIS PORTFOLIO — Immersive 3D Developer Portfolio: Immersive developer portfolio with a 3D dome gallery, scroll-driven animations, and an editorial bronze design system. Next.js + Three.js + custom design tokens.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-surface-raised { fill: #111111; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 11px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; }
      .ayu-text-heading { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 14px; font-weight: 600; }
      .ayu-text-label { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; font-weight: 500; }
      .ayu-success { fill: #22C55E; }
      .ayu-warning { fill: #EAB308; }
      .ayu-error { fill: #EF4444; }
      .ayu-info { fill: #38BDF8; }
      .ayu-chip-bg { fill: #1A1A1A; }
      .ayu-chip-border { fill: none; stroke: #27272A; stroke-width: 1; }
      .ayu-chip-text { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-metric-value { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 18px; font-weight: 600; }
      .ayu-metric-label { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-link { fill: #DC2626; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; text-decoration: underline; }
    </style>
  </defs>

  <rect class="ayu-surface" width="1000" height="280" rx="12"/>
  <rect class="ayu-border" width="1000" height="280" rx="12"/>

  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 268 L 28 252 L 12 252"/>
    <path class="ayu-accent" d="M 972 268 L 972 252 L 988 252"/>
  </g>

  <g id="ayu-header" transform="translate(32, 32)">
    <text class="ayu-text-heading" x="0" y="0">THIS PORTFOLIO — Immersive 3D Developer Portfolio</text>
    <g transform="translate(600, -14)">
      <rect class="ayu-chip-bg" width="120" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="120" height="28" rx="6"/>
      <circle fill="#22C55E" cx="16" cy="14" r="4"/>
      <text class="ayu-chip-text" x="24" y="18">ACTIVE</text>
    </g>
    <g transform="translate(740, -14)">
      <rect class="ayu-chip-bg" width="80" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="80" height="28" rx="6"/>
      <text class="ayu-chip-text" x="40" y="18" text-anchor="middle">SOLO</text>
    </g>
    <g transform="translate(840, -14)">
      <rect class="ayu-chip-bg" width="60" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="60" height="28" rx="6"/>
      <text class="ayu-chip-text" x="30" y="18" text-anchor="middle">★ 0</text>
    </g>
  </g>

  <line class="ayu-separator" x1="32" y1="60" x2="968" y2="60"/>

  <g id="ayu-description" transform="translate(32, 72)">
    <text class="ayu-text-primary" x="0" y="0" style="font-size: 11px;">Immersive developer portfolio with a 3D dome gallery, scroll-driven animations, and an editorial bronze design system. Next.js + Three.js + custom design tokens.</text>
  </g>

  <g id="ayu-tech-stack" transform="translate(32, 110)">
    <text class="ayu-text-muted" x="0" y="0">TECH</text>
    <g id="ayu-tech-tags" transform="translate(50, -6)">
      <g transform="translate(0, 0)">
  <rect class="ayu-chip-bg" width="65" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="65" height="22" rx="4"/>
  <text class="ayu-chip-text" x="32" y="15" text-anchor="middle">Next.js</text>
</g>
<g transform="translate(73, 0)">
  <rect class="ayu-chip-bg" width="86" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="86" height="22" rx="4"/>
  <text class="ayu-chip-text" x="43" y="15" text-anchor="middle">TypeScript</text>
</g>
<g transform="translate(167, 0)">
  <rect class="ayu-chip-bg" width="72" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="72" height="22" rx="4"/>
  <text class="ayu-chip-text" x="36" y="15" text-anchor="middle">Three.js</text>
</g>
<g transform="translate(247, 0)">
  <rect class="ayu-chip-bg" width="135" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="135" height="22" rx="4"/>
  <text class="ayu-chip-text" x="67" y="15" text-anchor="middle">React Three Fiber</text>
</g>
<g transform="translate(390, 0)">
  <rect class="ayu-chip-bg" width="44" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="44" height="22" rx="4"/>
  <text class="ayu-chip-text" x="22" y="15" text-anchor="middle">GSAP</text>
</g>
<g transform="translate(442, 0)">
  <rect class="ayu-chip-bg" width="100" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="100" height="22" rx="4"/>
  <text class="ayu-chip-text" x="50" y="15" text-anchor="middle">Tailwind CSS</text>
</g>
<g transform="translate(550, 0)">
  <rect class="ayu-chip-bg" width="107" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="107" height="22" rx="4"/>
  <text class="ayu-chip-text" x="53" y="15" text-anchor="middle">Design Tokens</text>
</g>
    </g>
  </g>

  <g id="ayu-highlights" transform="translate(32, 150)">
    <text class="ayu-text-muted" x="0" y="0">HIGHLIGHTS</text>
    <g transform="translate(50, 0)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Custom 3D dome gallery with 60fps mobile target</text>
</g>
<g transform="translate(50, 20)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Editorial bronze design system (tokens + components)</text>
</g>
<g transform="translate(50, 40)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Scroll-driven narrative animations</text>
</g>
<g transform="translate(50, 60)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Progressive enhancement — works without JS</text>
</g>
  </g>

  <g id="ayu-metrics" transform="translate(32, 210)">
    <line class="ayu-separator" x1="0" y1="-8" x2="936" y2="-8"/>
    <g class="ayu-metric" transform="translate(100, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">—</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">FILES</text>
</g>
<g class="ayu-metric" transform="translate(300, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">0</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STARS</text>
</g>
<g class="ayu-metric" transform="translate(500, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">MIT</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">LICENSE</text>
</g>
<g class="ayu-metric" transform="translate(700, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">2024-07</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">SINCE</text>
</g>
<g class="ayu-metric" transform="translate(900, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">ACTIVE</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STATUS</text>
</g>
  </g>

  <line class="ayu-separator" x1="32" y1="248" x2="968" y2="248"/>
  <g id="ayu-footer" transform="translate(32, 258)">
    <text class="ayu-text-muted" x="0" y="0">REPO:</text>
    <a href="https://github.com/AyuShetty/ayushetty.me" target="_blank">
      <text class="ayu-link" x="50" y="0">https://github.com/AyuShetty/ayushetty.me</text>
    </a>
  </g>
</svg>

</div>

---

<div align="center">
<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Project Card Component
Purpose: Reusable project showcase card for featured projects
Composes: panel, chip, divider
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 280" role="img">
  <title>AYU.OS — This Profile as an Operating System — AYU.OS Project</title>
  <desc>Project card for AYU.OS — This Profile as an Operating System: A fictional operating system expressed through a GitHub profile. Component-driven SVG design system, automated build pipeline, and token-based theming.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-surface-raised { fill: #111111; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 11px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; }
      .ayu-text-heading { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 14px; font-weight: 600; }
      .ayu-text-label { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; font-weight: 500; }
      .ayu-success { fill: #22C55E; }
      .ayu-warning { fill: #EAB308; }
      .ayu-error { fill: #EF4444; }
      .ayu-info { fill: #38BDF8; }
      .ayu-chip-bg { fill: #1A1A1A; }
      .ayu-chip-border { fill: none; stroke: #27272A; stroke-width: 1; }
      .ayu-chip-text { fill: #D4D4D8; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-metric-value { fill: #FAFAFA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 18px; font-weight: 600; }
      .ayu-metric-label { fill: #A1A1AA; font-family: "JetBrains Mono", Menlo, monospace; font-size: 9px; }
      .ayu-link { fill: #DC2626; font-family: "JetBrains Mono", Menlo, monospace; font-size: 10px; text-decoration: underline; }
    </style>
  </defs>

  <rect class="ayu-surface" width="1000" height="280" rx="12"/>
  <rect class="ayu-border" width="1000" height="280" rx="12"/>

  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 268 L 28 252 L 12 252"/>
    <path class="ayu-accent" d="M 972 268 L 972 252 L 988 252"/>
  </g>

  <g id="ayu-header" transform="translate(32, 32)">
    <text class="ayu-text-heading" x="0" y="0">AYU.OS — This Profile as an Operating System</text>
    <g transform="translate(600, -14)">
      <rect class="ayu-chip-bg" width="120" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="120" height="28" rx="6"/>
      <circle fill="#22C55E" cx="16" cy="14" r="4"/>
      <text class="ayu-chip-text" x="24" y="18">ACTIVE</text>
    </g>
    <g transform="translate(740, -14)">
      <rect class="ayu-chip-bg" width="80" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="80" height="28" rx="6"/>
      <text class="ayu-chip-text" x="40" y="18" text-anchor="middle">SOLO</text>
    </g>
    <g transform="translate(840, -14)">
      <rect class="ayu-chip-bg" width="60" height="28" rx="6"/>
      <rect class="ayu-chip-border" width="60" height="28" rx="6"/>
      <text class="ayu-chip-text" x="30" y="18" text-anchor="middle">★ 0</text>
    </g>
  </g>

  <line class="ayu-separator" x1="32" y1="60" x2="968" y2="60"/>

  <g id="ayu-description" transform="translate(32, 72)">
    <text class="ayu-text-primary" x="0" y="0" style="font-size: 11px;">A fictional operating system expressed through a GitHub profile. Component-driven SVG design system, automated build pipeline, and token-based theming.</text>
  </g>

  <g id="ayu-tech-stack" transform="translate(32, 110)">
    <text class="ayu-text-muted" x="0" y="0">TECH</text>
    <g id="ayu-tech-tags" transform="translate(50, -6)">
      <g transform="translate(0, 0)">
  <rect class="ayu-chip-bg" width="58" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="58" height="22" rx="4"/>
  <text class="ayu-chip-text" x="29" y="15" text-anchor="middle">Python</text>
</g>
<g transform="translate(66, 0)">
  <rect class="ayu-chip-bg" width="37" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="37" height="22" rx="4"/>
  <text class="ayu-chip-text" x="18" y="15" text-anchor="middle">SVG</text>
</g>
<g transform="translate(111, 0)">
  <rect class="ayu-chip-bg" width="58" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="58" height="22" rx="4"/>
  <text class="ayu-chip-text" x="29" y="15" text-anchor="middle">Jinja2</text>
</g>
<g transform="translate(177, 0)">
  <rect class="ayu-chip-bg" width="114" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="114" height="22" rx="4"/>
  <text class="ayu-chip-text" x="57" y="15" text-anchor="middle">GitHub Actions</text>
</g>
<g transform="translate(299, 0)">
  <rect class="ayu-chip-bg" width="107" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="107" height="22" rx="4"/>
  <text class="ayu-chip-text" x="53" y="15" text-anchor="middle">Design Tokens</text>
</g>
<g transform="translate(414, 0)">
  <rect class="ayu-chip-bg" width="44" height="22" rx="4"/>
  <rect class="ayu-chip-border" width="44" height="22" rx="4"/>
  <text class="ayu-chip-text" x="22" y="15" text-anchor="middle">SVGO</text>
</g>
    </g>
  </g>

  <g id="ayu-highlights" transform="translate(32, 150)">
    <text class="ayu-text-muted" x="0" y="0">HIGHLIGHTS</text>
    <g transform="translate(50, 0)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">15+ reusable SVG primitives with validation</text>
</g>
<g transform="translate(50, 20)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Fully automated daily stats refresh via GitHub Actions</text>
</g>
<g transform="translate(50, 40)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">WCAG 2.1 AA accessible SVGs</text>
</g>
<g transform="translate(50, 60)">
  <circle class="ayu-success" cx="0" cy="9" r="3"/>
  <text class="ayu-text-primary" x="10" y="13" style="font-size: 10px;">Token-driven theming system</text>
</g>
  </g>

  <g id="ayu-metrics" transform="translate(32, 210)">
    <line class="ayu-separator" x1="0" y1="-8" x2="936" y2="-8"/>
    <g class="ayu-metric" transform="translate(100, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">—</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">FILES</text>
</g>
<g class="ayu-metric" transform="translate(300, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">0</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STARS</text>
</g>
<g class="ayu-metric" transform="translate(500, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">MIT</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">LICENSE</text>
</g>
<g class="ayu-metric" transform="translate(700, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">2024-07</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">SINCE</text>
</g>
<g class="ayu-metric" transform="translate(900, 0)">
  <text class="ayu-metric-value" x="0" y="18" text-anchor="middle">ACTIVE</text>
  <text class="ayu-metric-label" x="0" y="34" text-anchor="middle">STATUS</text>
</g>
  </g>

  <line class="ayu-separator" x1="32" y1="248" x2="968" y2="248"/>
  <g id="ayu-footer" transform="translate(32, 258)">
    <text class="ayu-text-muted" x="0" y="0">REPO:</text>
    <a href="https://github.com/AyuShetty/AyuShetty" target="_blank">
      <text class="ayu-link" x="50" y="0">https://github.com/AyuShetty/AyuShetty</text>
    </a>
  </g>
</svg>

</div>

---

---

<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Header Component
Purpose: Page header with title and status
Version: 2.0
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 80" role="img">
  <title>EXPERIENCE TIMELINE — AYU.OS</title>
  <desc>Career progression. Newest first.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: Menlo, monospace; font-size: 14px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: Menlo, monospace; font-size: 10px; }
      .ayu-success { fill: #22C55E; }
    </style>
  </defs>
  <!-- Background -->
  <rect class="ayu-surface" width="1000" height="80" rx="12"/>
  <rect class="ayu-border" width="1000" height="80" rx="12"/>
  <!-- Corner Accents -->
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 68 L 28 52 L 12 52"/>
    <path class="ayu-accent" d="M 972 68 L 972 52 L 988 52"/>
  </g>
  <!-- Title -->
  <g id="ayu-title-group">
    <text class="ayu-text-primary" x="32" y="36">EXPERIENCE TIMELINE</text>
    <text class="ayu-text-muted" x="32" y="56">Career progression. Newest first.</text>
  </g>
  <!-- Status -->
  <g id="ayu-status-group">
    <circle class="ayu-success" cx="920" cy="36" r="4"/>
    <text class="ayu-text-muted" x="936" y="40">ACTIVE</text>
  </g>
  <!-- Separator -->
  <g id="ayu-separator-group">
    <line class="ayu-separator" x1="32" y1="68" x2="968" y2="68"/>
  </g>
</svg>


### Product Engineer at Avarch
*2023-01 – Present | Bangalore, India (Remote)*
Leading product engineering for Web3 and AI platforms. Architected EIPSINSIGHT governance analytics platform. Building LOCAL AI INFRASTRUCTURE for distributed local LLM inference. Exploring MPC/TSS cryptography for secure key management.

**Key Achievements:**
- Architected EIPSINSIGHT — Ethereum governance analytics platform tracking EIP lifecycles and governance signals in real-time
- Built LOCAL AI INFRASTRUCTURE — distributed multi-node local LLM orchestration with Playwright browser automation and Open WebUI integration
- Developed AI WORKFLOW AUTOMATION — framework integrating local AI models with browser automation for repetitive engineering tasks
- Contributed to Ethereum Foundation grant milestones for governance tooling
- Published 200+ Ethereum research articles and governance analyses
- Won ENS Pool Prize at ETHMumbai 2026 hackathon
- Led team of 4 engineers on Web3 product initiatives

**Technologies:** TypeScript, Next.js, React, Python, Ollama, Playwright, Solidity, Ethereum, Docker, Kubernetes, PostgreSQL, Redis, GitHub Actions

---

### President at COPE (Community of Peer Engineers)
*2022-01 – 2023-12 | Bangalore, India*
Led 200+ member student engineering community. Organized hackathons, workshops, and industry mentorship programs. Built internal tools for community management.

**Key Achievements:**
- Scaled community from 50 to 200+ active members
- Organized 12+ hackathons and technical workshops
- Secured sponsorship from 8+ tech companies
- Built community management platform with automated event workflows
- Mentored 50+ students in full-stack and blockchain development

**Technologies:** React, Node.js, TypeScript, PostgreSQL, Docker, GitHub Actions

---

### Software Engineering Intern at Avarch
*2021-06 – 2022-12 | Bangalore, India*
Early contributor to EIPSINSIGHT platform. Full-stack development on Ethereum governance tooling. Research on EIP analysis methodologies.

**Key Achievements:**
- Built initial EIPSINSIGHT frontend with React + TypeScript
- Implemented EIP lifecycle tracking with on-chain data ingestion
- Research on Ethereum governance mechanisms and stakeholder analysis
- Contributed to ETH.ED platform architecture (AI-powered Web3 learning)

**Technologies:** React, TypeScript, Ethereum, Solidity, The Graph, Node.js, PostgreSQL

---

### B.Tech Information Science & Engineering at NMAM Institute of Technology (VTU)
*2017-08 – 2021-05 | Nitte, Karnataka, India*
Focus: Distributed Systems, Compilers, Cryptography, Computer Networks. Final year thesis: 'Efficient State Synchronization in Byzantine Environments'. Active in ACM student chapter.

**Key Achievements:**
- Published research on consensus optimization at [Conference]
- Built experimental blockchain runtime in Rust for thesis
- Teaching Assistant for Operating Systems & Computer Networks
- ACM Student Chapter Vice Chair — organized 15+ technical events
- Google Developer Student Club Core Team member
- Finalist at Smart India Hackathon 2020

**Technologies:** Rust, C++, Go, Linux Kernel, Distributed Systems, Cryptography, Compilers

---

---

<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Header Component
Purpose: Page header with title and status
Version: 2.0
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 80" role="img">
  <title>RESEARCH — AYU.OS</title>
  <desc>Current areas of interest and investigation.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: Menlo, monospace; font-size: 14px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: Menlo, monospace; font-size: 10px; }
      .ayu-success { fill: #22C55E; }
    </style>
  </defs>
  <!-- Background -->
  <rect class="ayu-surface" width="1000" height="80" rx="12"/>
  <rect class="ayu-border" width="1000" height="80" rx="12"/>
  <!-- Corner Accents -->
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 68 L 28 52 L 12 52"/>
    <path class="ayu-accent" d="M 972 68 L 972 52 L 988 52"/>
  </g>
  <!-- Title -->
  <g id="ayu-title-group">
    <text class="ayu-text-primary" x="32" y="36">RESEARCH</text>
    <text class="ayu-text-muted" x="32" y="56">Current areas of interest and investigation.</text>
  </g>
  <!-- Status -->
  <g id="ayu-status-group">
    <circle class="ayu-success" cx="920" cy="36" r="4"/>
    <text class="ayu-text-muted" x="936" y="40">ACTIVE</text>
  </g>
  <!-- Separator -->
  <g id="ayu-separator-group">
    <line class="ayu-separator" x1="32" y1="68" x2="968" y2="68"/>
  </g>
</svg>


### Local LLM Orchestration
Efficient inference pipelines, speculative decoding, and model routing for on-device agent workloads. Building production-grade local AI infrastructure.

Links: [LOCAL AI INFRASTRUCTURE Repo](https://github.com/AyuShetty/local_ai_infrastructure) | [AI Workflow Automation Repo](https://github.com/AyuShetty/ai_workflow_automation)

---

### Ethereum Protocol Analysis
Static analysis, formal verification, and gas optimization for EIPs and core protocol changes. Governance analytics for transparent decision-making.

Links: [EIPSINSIGHT Platform](https://github.com/AyuShetty/eipsinsight) | [EIP Diagnostics (Legacy)](https://github.com/AyuShetty/eip_diagnostics)

---

### Systems Design & Developer Infrastructure
Patterns for scalable, maintainable developer tooling: monorepos, CI/CD, observability, automation, and platform engineering.

Links: [Dev Toolkit (Legacy)](https://github.com/AyuShetty/dev_toolkit)

---

### Design Systems & SVG Engineering
Token-driven, accessible SVG component libraries with programmatic composition. Treating design systems as engineering products.

Links: [AYU.OS Design System](https://github.com/AyuShetty/AyuShetty/tree/main/components) | [Portfolio 3D Design System](https://github.com/AyuShetty/portfolio)

---

### Biometric Cryptography & Post-Quantum Security
Novel key derivation from biometric features for post-quantum cryptographic primitives. Intersection of computer vision and cryptography.

Links: [FACIAL KEYGEN Repo](https://github.com/AyuShetty/facial_keygen)

---

### Human-Computer Interaction (Touchless Interfaces)
Real-time gesture recognition for presentation control and accessibility. MediaPipe + OpenCV pipelines for edge deployment.

Links: [AIRGESTURE Repo](https://github.com/AyuShetty/airgesture)

---

---

<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Header Component
Purpose: Page header with title and status
Version: 2.0
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 80" role="img">
  <title>CURRENT OBJECTIVES — AYU.OS</title>
  <desc>Active missions and focus areas.</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: Menlo, monospace; font-size: 14px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: Menlo, monospace; font-size: 10px; }
      .ayu-success { fill: #22C55E; }
    </style>
  </defs>
  <!-- Background -->
  <rect class="ayu-surface" width="1000" height="80" rx="12"/>
  <rect class="ayu-border" width="1000" height="80" rx="12"/>
  <!-- Corner Accents -->
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 68 L 28 52 L 12 52"/>
    <path class="ayu-accent" d="M 972 68 L 972 52 L 988 52"/>
  </g>
  <!-- Title -->
  <g id="ayu-title-group">
    <text class="ayu-text-primary" x="32" y="36">CURRENT OBJECTIVES</text>
    <text class="ayu-text-muted" x="32" y="56">Active missions and focus areas.</text>
  </g>
  <!-- Status -->
  <g id="ayu-status-group">
    <circle class="ayu-success" cx="920" cy="36" r="4"/>
    <text class="ayu-text-muted" x="936" y="40">ACTIVE</text>
  </g>
  <!-- Separator -->
  <g id="ayu-separator-group">
    <line class="ayu-separator" x1="32" y1="68" x2="968" y2="68"/>
  </g>
</svg>


- 🔄 **Ship LOCAL AI INFRASTRUCTURE v1.0 — Production-Ready Distributed Inference** (65%)
  Complete the distributed local LLM orchestration platform with multi-node inference, browser automation integration, and Open WebUI compatibility. Target: zero-config Docker deployment.
  Target: 2025-03-01

- 📋 **EIPSINSIGHT v2 — Real-time Governance Intelligence** (15%)
  Expand EIPsInsight to cover EOF, Verkle trees, and upcoming protocol upgrades. Add predictive governance signaling and stakeholder influence mapping.
  Target: 2025-06-01

- 🔄 **Open-Source AYU.OS Design System with Plugin Architecture** (40%)
  Extract the SVG component library, token system, and composition engine as a standalone OSS package. Enable theming, custom primitives, and framework-agnostic usage.
  Target: 2025-04-15

- 🔄 **Publish FACIAL KEYGEN Research — Biometric Key Derivation for Post-Quantum Crypto** (30%)
  Formalize the biometric-to-cryptographic-key derivation pipeline. Submit to cryptography conference. Open-source reproducible implementation with security analysis.
  Target: 2025-05-01

- 📋 **Portfolio 3D Optimization — 60fps on Mobile, <100KB Bundle** (10%)
  Optimize the 3D dome gallery for mobile performance. Implement progressive enhancement, WASM physics, and aggressive bundle splitting.
  Target: 2025-03-15

---

<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Header Component
Purpose: Page header with title and status
Version: 2.0
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 80" role="img">
  <title>TERMINAL — AYU.OS</title>
  <desc>Interactive command reference</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: Menlo, monospace; font-size: 14px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: Menlo, monospace; font-size: 10px; }
      .ayu-success { fill: #22C55E; }
    </style>
  </defs>
  <!-- Background -->
  <rect class="ayu-surface" width="1000" height="80" rx="12"/>
  <rect class="ayu-border" width="1000" height="80" rx="12"/>
  <!-- Corner Accents -->
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 68 L 28 52 L 12 52"/>
    <path class="ayu-accent" d="M 972 68 L 972 52 L 988 52"/>
  </g>
  <!-- Title -->
  <g id="ayu-title-group">
    <text class="ayu-text-primary" x="32" y="36">TERMINAL</text>
    <text class="ayu-text-muted" x="32" y="56">Interactive command reference</text>
  </g>
  <!-- Status -->
  <g id="ayu-status-group">
    <circle class="ayu-success" cx="920" cy="36" r="4"/>
    <text class="ayu-text-muted" x="936" y="40">ACTIVE</text>
  </g>
  <!-- Separator -->
  <g id="ayu-separator-group">
    <line class="ayu-separator" x1="32" y1="68" x2="968" y2="68"/>
  </g>
</svg>


```text
$ ayu-os init
[OK] Kernel synchronized.
[OK] Modules loaded: 8 active.
[OK] AI Core initialized — Local LLM ready.
[OK] Ethereum module loaded — EIPSINSIGHT connected.
[OK] Automation engine online — Playwright + Ollama.
> System ready. Awaiting input...
$ 
```

---

<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Header Component
Purpose: Page header with title and status
Version: 2.0
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 80" role="img">
  <title>TELEMETRY — AYU.OS</title>
  <desc>GitHub statistics and system metrics</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: Menlo, monospace; font-size: 14px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: Menlo, monospace; font-size: 10px; }
      .ayu-success { fill: #22C55E; }
    </style>
  </defs>
  <!-- Background -->
  <rect class="ayu-surface" width="1000" height="80" rx="12"/>
  <rect class="ayu-border" width="1000" height="80" rx="12"/>
  <!-- Corner Accents -->
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 68 L 28 52 L 12 52"/>
    <path class="ayu-accent" d="M 972 68 L 972 52 L 988 52"/>
  </g>
  <!-- Title -->
  <g id="ayu-title-group">
    <text class="ayu-text-primary" x="32" y="36">TELEMETRY</text>
    <text class="ayu-text-muted" x="32" y="56">GitHub statistics and system metrics</text>
  </g>
  <!-- Status -->
  <g id="ayu-status-group">
    <circle class="ayu-success" cx="920" cy="36" r="4"/>
    <text class="ayu-text-muted" x="936" y="40">ACTIVE</text>
  </g>
  <!-- Separator -->
  <g id="ayu-separator-group">
    <line class="ayu-separator" x1="32" y1="68" x2="968" y2="68"/>
  </g>
</svg>


- **Public Repositories:** 19
- **Total Stars:** 4
- **Total Forks:** 2
- **Commits (1yr):** 391
- **Followers:** 4
- **Following:** 9
- **Current Streak:** 10 days
- **Longest Streak:** 10 days

**Top Languages:**
- TypeScript: 84.7%
- JavaScript: 4.9%
- Swift: 4.3%
- CSS: 2.8%
- Python: 1.5%

---

<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Header Component
Purpose: Page header with title and status
Version: 2.0
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 80" role="img">
  <title>TELEMETRY — AYU.OS</title>
  <desc>GitHub statistics and system metrics</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: Menlo, monospace; font-size: 14px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: Menlo, monospace; font-size: 10px; }
      .ayu-success { fill: #22C55E; }
    </style>
  </defs>
  <!-- Background -->
  <rect class="ayu-surface" width="1000" height="80" rx="12"/>
  <rect class="ayu-border" width="1000" height="80" rx="12"/>
  <!-- Corner Accents -->
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 68 L 28 52 L 12 52"/>
    <path class="ayu-accent" d="M 972 68 L 972 52 L 988 52"/>
  </g>
  <!-- Title -->
  <g id="ayu-title-group">
    <text class="ayu-text-primary" x="32" y="36">TELEMETRY</text>
    <text class="ayu-text-muted" x="32" y="56">GitHub statistics and system metrics</text>
  </g>
  <!-- Status -->
  <g id="ayu-status-group">
    <circle class="ayu-success" cx="920" cy="36" r="4"/>
    <text class="ayu-text-muted" x="936" y="40">ACTIVE</text>
  </g>
  <!-- Separator -->
  <g id="ayu-separator-group">
    <line class="ayu-separator" x1="32" y1="68" x2="968" y2="68"/>
  </g>
</svg>


- **Public Repositories:** 19
- **Total Stars:** 4
- **Total Forks:** 2
- **Commits (1yr):** 391
- **Followers:** 4
- **Following:** 9
- **Current Streak:** 10 days
- **Longest Streak:** 10 days

**Top Languages:**
- TypeScript: 84.7%
- JavaScript: 4.9%
- Swift: 4.3%
- CSS: 2.8%
- Python: 1.5%

---

<?xml version="1.0" encoding="UTF-8"?>
<!-- AYU.OS - Header Component
Purpose: Page header with title and status
Version: 2.0
Spec: COMPONENT_SPEC.md, TOKENS.md
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 80" role="img">
  <title>CONTACT — AYU.OS</title>
  <desc>Establish connection</desc>
  <defs>
    <style>
      .ayu-surface { fill: #09090B; }
      .ayu-border { fill: none; stroke: #27272A; stroke-width: 1.5; stroke-linejoin: round; stroke-linecap: round; }
      .ayu-accent { fill: none; stroke: #DC2626; stroke-width: 1.5; opacity: 0.6; stroke-linecap: round; stroke-linejoin: round; }
      .ayu-separator { stroke: #27272A; stroke-width: 1.5; }
      .ayu-text-primary { fill: #FAFAFA; font-family: Menlo, monospace; font-size: 14px; }
      .ayu-text-muted { fill: #A1A1AA; font-family: Menlo, monospace; font-size: 10px; }
      .ayu-success { fill: #22C55E; }
    </style>
  </defs>
  <!-- Background -->
  <rect class="ayu-surface" width="1000" height="80" rx="12"/>
  <rect class="ayu-border" width="1000" height="80" rx="12"/>
  <!-- Corner Accents -->
  <g id="ayu-corner-group">
    <path class="ayu-accent" d="M 28 12 L 28 28 L 12 28"/>
    <path class="ayu-accent" d="M 972 12 L 972 28 L 988 28"/>
    <path class="ayu-accent" d="M 28 68 L 28 52 L 12 52"/>
    <path class="ayu-accent" d="M 972 68 L 972 52 L 988 52"/>
  </g>
  <!-- Title -->
  <g id="ayu-title-group">
    <text class="ayu-text-primary" x="32" y="36">CONTACT</text>
    <text class="ayu-text-muted" x="32" y="56">Establish connection</text>
  </g>
  <!-- Status -->
  <g id="ayu-status-group">
    <circle class="ayu-success" cx="920" cy="36" r="4"/>
    <text class="ayu-text-muted" x="936" y="40">ACTIVE</text>
  </g>
  <!-- Separator -->
  <g id="ayu-separator-group">
    <line class="ayu-separator" x1="32" y1="68" x2="968" y2="68"/>
  </g>
</svg>


- **GitHub**: [AyuShetty](https://github.com/AyuShetty) ★
- **Email**: [ayush@ayushetty.me](mailto:ayush@ayushetty.me) ★
- **Website / Portfolio**: [ayushetty.me](https://ayushetty.me) ★
- **LinkedIn**: [ayushetty](https://linkedin.com/in/ayushetty)
- **X (Twitter)**: [@AyuShettyEth](https://x.com/AyuShettyEth)
- **Instagram**: [ayushetty.eth](https://instagram.com/ayushetty.eth)

*Preferred: GitHub Issues or Email*

---

> Shipping real products. Exploring MPC/TSS security. Code that actually scales.

> Repository Version: v2.0.0
> Last Generated: 2026-08-12T11:29:56.453616Z

[![Built with AYU.OS](https://img.shields.io/badge/Built%20with-AYU.OS-DC2626?style=flat-square)](https://github.com/AyuShetty/AyuShetty)
