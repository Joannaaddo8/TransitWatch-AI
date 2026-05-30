import pandas as pd
from pathlib import Path

BASE_PATH = Path("app/data/gtfs_static")

def load_gtfs_data():
    routes = pd.read_csv(BASE_PATH / "routes.txt")
    trips = pd.read_csv(BASE_PATH / "trips.txt")
    stops = pd.read_csv(BASE_PATH / "stops.txt")

    # ⚠️ DO NOT load full stop_times yet (too big)
    stop_times = pd.read_csv(BASE_PATH / "stop_times.txt", nrows=50000)

    return {
        "routes": routes,
        "trips": trips,
        "stops": stops,
        "stop_times": stop_times
    }