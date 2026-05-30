from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_dashboard import router as dashboard_router
from app.api.routes_insights import router as insights_router
from app.api.routes_ranking import router as ranking_router
from app.api.routes_shapes import router as shapes_router
from app.api.routes_vehicles import router as vehicles_router
from app.api.routes_crew_ai import router as crew_ai_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard_router)
app.include_router(insights_router)
app.include_router(ranking_router)
app.include_router(shapes_router)
app.include_router(vehicles_router)
app.include_router(crew_ai_router)


@app.get("/")
def root():
    return {"message": "TransitWatch AI Backend is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}