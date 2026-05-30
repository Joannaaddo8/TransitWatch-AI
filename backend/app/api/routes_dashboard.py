from fastapi import APIRouter
from app.services.kpi_generator import generate_kpis

router = APIRouter()


@router.get("/dashboard")
def get_dashboard():
    return {
        "status": "success",
        "data": generate_kpis()
    }