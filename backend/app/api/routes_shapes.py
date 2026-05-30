from fastapi import APIRouter
from app.services.analytics_engine import analyze_transit_data
from app.services.insights_engine import generate_insights

router = APIRouter()


@router.get("/insights")
def get_insights():
    analysis = analyze_transit_data()
    insights = generate_insights(analysis)

    return {
        "status": "success",
        "insights": insights
    }