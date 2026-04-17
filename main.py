import requests
import time
import json
import os
import random
import sys

def read_statuses(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except Exception:
        sys.exit()

def run():
    config = load_config()
    token = config.get("token")
    clear_enabled = config.get("clear_enabled", False)
    clear_interval = config.get("clear_interval", 60)
    sleep_interval = config.get("sleep_interval", 1)
    is_random = config.get("random")

    if is_random is None:
        sys.exit()

    statuses = read_statuses("statuses.txt")
    if not statuses:
        sys.exit()

    session = requests.Session()
    session.headers.update({'authorization': token})

    status_count = 0
    status_index = 0

    try:
        while True:
            try:
                if is_random:
                    current_status = random.choice(statuses)
                else:
                    current_status = statuses[status_index]
                    status_index = (status_index + 1) % len(statuses)

                settings_res = session.get("https://discord.com/api/v8/users/@me/settings", timeout=10)
                if settings_res.status_code != 200:
                    time.sleep(5)
                    continue

                settings = settings_res.json()
                custom_status = settings.get("custom_status") or {}
                custom_status["text"] = current_status

                payload = {
                    "custom_status": custom_status,
                    "activities": settings.get("activities", [])
                }

                patch_res = session.patch("https://discord.com/api/v8/users/@me/settings", json=payload, timeout=10)
                
                if patch_res.status_code == 200:
                    print(f"{time.strftime('%I:%M %p')}: Status -> {current_status}")
                    status_count += 1
                
                if clear_enabled and status_count % clear_interval == 0:
                    clear_console()

                wait_time = random.uniform(0.1, sleep_interval) if is_random else sleep_interval
                time.sleep(wait_time)

            except (requests.RequestException, json.JSONDecodeError):
                time.sleep(5)
                continue

    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    run()