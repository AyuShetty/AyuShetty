
def get_modules():
    return [
        {
            "name": "Kernel",
            "status": "active",
            "desc": "System initialization and runtime management.",
            "icon": "kernel"
        },
        {
            "name": "Mission Control",
            "status": "active",
            "desc": "Active projects and career timeline.",
            "icon": "mission"
        },
        {
            "name": "AI Core",
            "status": "active",
            "desc": "Reasoning engine and local LLM orchestration.",
            "icon": "brain"
        },
        {
            "name": "Research Database",
            "status": "active",
            "desc": "Articles, blogs, and documentation.",
            "icon": "research"
        },
        {
            "name": "Filesystem",
            "status": "active",
            "desc": "Public repositories and subsystems.",
            "icon": "database"
        },
        {
            "name": "Telemetry",
            "status": "active",
            "desc": "GitHub statistics and system metrics.",
            "icon": "signal"
        },
        {
            "name": "Network",
            "status": "standby",
            "desc": "Connections and packet routing.",
            "icon": "network"
        },
        {
            "name": "Archive",
            "status": "standby",
            "desc": "Past work and deprecated modules.",
            "icon": "archive"
        }
    ]
