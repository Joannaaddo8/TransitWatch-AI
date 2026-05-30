import pandas as pd
import os

ROUTES_TO_KEEP = [
    "29","35","39","53","60","68","85","86",
    "95","102","116","129","134","165",
    "300","320","501","504","505","506",
    "509","510","512","927"
]

trips = pd.read_csv("app/data/gtfs_static/trips.txt")

trip_ids = trips[
    trips["route_id"].astype(str).isin(ROUTES_TO_KEEP)
]["trip_id"]

print(f"Trips selected: {len(trip_ids)}")

stop_times = pd.read_csv(
    "app/data/gtfs_static/stop_times.txt"
)

reduced = stop_times[
    stop_times["trip_id"].isin(trip_ids)
]

output_file = "app/data/gtfs_static/stop_times_reduced.txt"

reduced.to_csv(output_file, index=False)

original_size = os.path.getsize(
    "app/data/gtfs_static/stop_times.txt"
) / (1024 * 1024)

reduced_size = os.path.getsize(
    output_file
) / (1024 * 1024)

print(f"Original size: {original_size:.2f} MB")
print(f"Reduced size: {reduced_size:.2f} MB")
print(f"Rows kept: {len(reduced)}")