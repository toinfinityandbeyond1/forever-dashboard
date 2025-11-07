import json, datetime, random
import shutil

# Simulated data collection
data = {
    "timestamp": datetime.datetime.utcnow().isoformat(),
    "records_collected": random.randint(100, 2000),
    "status": "ok"
}

# Save to data folder
with open("data/status.json", "w") as f:
    json.dump(data, f, indent=2)
