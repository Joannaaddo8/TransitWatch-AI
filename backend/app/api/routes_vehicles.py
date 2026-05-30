from fastapi import APIRouter
from app.services.gtfs_realtime_loader import load_live_vehicles

router = APIRouter()


@router.get("/vehicles/live")
def get_live_vehicles():
    vehicles = load_live_vehicles(limit=50)

    return {
        "status": "success",
        "count": len(vehicles),
        "data": vehicles
    }