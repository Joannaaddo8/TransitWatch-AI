from fastapi import APIRouter
from app.services.analytics_engine import analyze_transit_data
from app.services.crew_ai_engine import generate_crew_ai_summary

router = APIRouter()


@router.get("/crew-ai/summary")
def get_crew_ai_summary():
    analysis = analyze_transit_data()
    summary = generate_crew_ai_summary(analysis)

    return {
        "status": "success",
        "data": summary
    }
