from datetime import datetime


LOG_FILE = "admin.log"


def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {action}\n")