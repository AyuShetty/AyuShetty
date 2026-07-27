
def get_logs(limit=5):
    logs = [
        {"time": "16:30:01", "level": "INFO", "msg": "System initialized"},
        {"time": "16:30:02", "level": "INFO", "msg": "Kernel synchronized"},
        {"time": "16:30:03", "level": "INFO", "msg": "AI Core loaded"},
        {"time": "16:30:04", "level": "WARN", "msg": "Network interface standby"},
        {"time": "16:30:05", "level": "INFO", "msg": "Mission control active"}
    ]
    return logs[:limit]
