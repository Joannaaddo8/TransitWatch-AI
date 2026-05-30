from fastapi import APIRouter
import pandas as pd
from functools import lru_cache

router = APIRouter()


@lru_cache(maxsize=1)
def load_route_shapes():
    shapes = pd.read_csv("app/data/gtfs_static/shapes.txt")
    trips = pd.read_csv("app/data/gtfs_static/trips.txt")

    route_to_shape = (
        trips[["route_id", "shape_id"]]
        .dropna()
        .drop_duplicates("route_id")
    )

    route_shapes = {}

    for _, route_row in route_to_shape.iterrows():
        route_id = str(route_row["route_id"])
        shape_id = route_row["shape_id"]

        shape_points = shapes[shapes["shape_id"] == shape_id]

        if shape_points.empty:
            continue

        shape_points = shape_points.sort_values("shape_pt_sequence")

        # Scale down points for speed
        shape_points = shape_points.iloc[::10]

        coordinates = []

        for _, point in shape_points.iterrows():
            coordinates.append([
                float(point["shape_pt_lat"]),
                float(point["shape_pt_lon"])
            ])

        route_shapes[route_id] = coordinates

        if len(route_shapes) >= 80:
            break

    return route_shapes


@router.get("/routes/shapes")
def get_route_shapes():
    return {
        "status": "success",
        "data": load_route_shapes()
    }