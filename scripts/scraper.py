import json, datetime, random, os

# --- Existing status.json logic ---
data = {
    "timestamp": datetime.datetime.utcnow().isoformat(),
    "records_collected": random.randint(100, 2000),
    "status": "ok"
}

with open("data/status.json", "w") as f:
    json.dump(data, f, indent=2)

# --- New: calculate GitHub repo usage ---
def get_repo_size(path="."):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            total += os.path.getsize(os.path.join(dirpath, f))
    return total / (1024*1024)  # MB

used_mb = get_repo_size()

storage = {
    "storage_options": [
        {
            "name": "GitHub",
            "max_storage": "1 GB",
            "used_storage": f"{used_mb:.2f} MB",
            "notes": "JSON logs, static data"
        },
        {
            "name": "Supabase",
            "max_storage": "500 MB",
            "used_storage": "unknown",
            "notes": "SQL tables, real-time updates"
        }
    ]
}

# Save to dashboard folder for Pages
with open("dashboard/storage.json", "w") as f:
    json.dump(storage, f, indent=2)
