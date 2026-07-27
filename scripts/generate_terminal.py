
def get_commands():
    return {
        "help": "Available commands: about, modules, skills, projects, contact, resume, github, status",
        "about": "AYU.OS v7.0.0 | Product Engineer | AI & Local LLM Architect | Ethereum Protocols",
        "modules": "Kernel | Mission Control | AI Core | Research | Filesystem | Telemetry | Network | Archive",
        "skills": "Python | TypeScript | Solidity | Playwright | Ollama | Docker | Systems Design",
        "projects": "browser_agents | eip_diagnostics | dev_toolkit | ayu_os",
        "contact": "email | github | twitter | linkedin",
        "resume": "Downloading resume...",
        "github": "https://github.com/AyuShetty",
        "status": "All systems operational. Kernel synchronized."
    }

def get_terminal_output():
    return """$ ayu-os init
[INFO] Kernel loaded successfully.
[INFO] Mounting filesystem...
[INFO] AI Core initialized.
[INFO] Network interface standby.
[OK] System ready.
$"""
