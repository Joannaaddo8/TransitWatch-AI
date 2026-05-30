import csv
import os


def load_transit_data(source="synthetic"):
    if source == "synthetic":
        return load_synthetic_data()

    if source == "gtfs":
        return load_gtfs_data()

    raise ValueError("Invalid data source selected")


def load_synthetic_data():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "../data/synthetic/transit_trips.csv"
    )

    scheduled_trips = []
    actual_trips = []

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            scheduled_trips.append({
                "route": row["route"],
                "hour": row["hour"],
                "scheduled_time": row["scheduled_time"]
            })

            actual_trips.append({
                "actual_delay": int(row["actual_delay"])
            })

    return scheduled_trips, actual_trips


def format_hour(hour_number):
    hour_number = hour_number % 24

    if hour_number == 0:
        return "12 AM"
    elif hour_number < 12:
        return f"{hour_number} AM"
    elif hour_number == 12:
        return "12 PM"
    else:
        return f"{hour_number - 12} PM"


def load_gtfs_data():
    routes_path = os.path.join(
        os.path.dirname(__file__),
        "../data/gtfs_static/routes.txt"
    )

    trips_path = os.path.join(
        os.path.dirname(__file__),
        "../data/gtfs_static/trips.txt"
    )

    stop_times_path = os.path.join(
        os.path.dirname(__file__),
        "../data/gtfs_static/stop_times.txt"
    )

    routes = {}
    trips = {}
    scheduled_trips = []
    actual_trips = []

    with open(routes_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            routes[row["route_id"]] = row["route_short_name"]

    with open(trips_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            trips[row["trip_id"]] = row["route_id"]

    with open(stop_times_path, mode="r") as file:
        reader = csv.DictReader(file)

        for index, row in enumerate(reader):
            if index >= 50000:
                break

            trip_id = row["trip_id"]

            if trip_id not in trips:
                continue

            route_id = trips[trip_id]

            if route_id not in routes:
                continue

            route_name = routes[route_id]
            scheduled_time = row["arrival_time"][:5]

            hour_number = int(scheduled_time.split(":")[0])
            hour_label = format_hour(hour_number)

            scheduled_trips.append({
                "route": route_name,
                "hour": hour_label,
                "scheduled_time": scheduled_time
            })

            actual_trips.append({
                "actual_delay": calculate_simulated_delay(route_name, hour_number)
            })

    return scheduled_trips, actual_trips


def calculate_simulated_delay(route_name, hour_number):
    if route_name.startswith("3"):
        base_delay = 0
    elif route_name.startswith("5"):
        base_delay = 2
    elif route_name.startswith("9"):
        base_delay = 1
    else:
        base_delay = 1

    peak_hours = [7, 8, 9, 16, 17]

    if hour_number in peak_hours:
        if route_name.startswith("5"):
            return base_delay + 6
        if route_name.startswith("9"):
            return base_delay + 4
        return base_delay + 3

    if route_name.startswith("3"):
        return 0

    if route_name.startswith("5"):
        return 1

    return 0