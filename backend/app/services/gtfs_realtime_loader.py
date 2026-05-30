import requests
from google.transit import gtfs_realtime_pb2

VEHICLE_POSITIONS_URL = "https://bustime.ttc.ca/gtfsrt/vehicles"


def load_live_vehicles(limit=50):
    feed = gtfs_realtime_pb2.FeedMessage()

    response = requests.get(VEHICLE_POSITIONS_URL, timeout=10)
    response.raise_for_status()

    feed.ParseFromString(response.content)

    vehicles = []

    for entity in feed.entity:
        if entity.HasField("vehicle"):
            vehicle = entity.vehicle

            if vehicle.HasField("position"):
                vehicles.append({
                    "vehicle_id": vehicle.vehicle.id,
                    "trip_id": vehicle.trip.trip_id,
                    "route_id": vehicle.trip.route_id,
                    "latitude": vehicle.position.latitude,
                    "longitude": vehicle.position.longitude,
                    "timestamp": vehicle.timestamp
                })

        if len(vehicles) >= limit:
            break

    return vehicles