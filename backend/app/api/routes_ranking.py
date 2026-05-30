from fastapi import APIRouter
from app.services.analytics_engine import analyze_transit_data
from app.services.route_ranking_service import get_top_worst_routes

router = APIRouter()


@router.get("/routes/worst")
def get_worst_routes():
    analysis = analyze_transit_data()
    worst_routes = get_top_worst_routes(analysis)

    return {
        "status": "success",
        "data": worst_routes
    }