import json, datetime, random

data = {
    "timestamp": datetime.datetime.utcnow().isoformat(),
    "uptime_days": random.randint(100, 5000),
    "scraper_status": "ok",
    "records_collected": random.randint(100, 2000),
}

with open("data/status.json", "w") as f:
    json.dump(data, f, indent=2)
