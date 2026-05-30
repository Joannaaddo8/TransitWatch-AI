# TransitWatch AI — Backend

TransitWatch AI is a smart transit reliability backend that processes transit trip data, generates performance KPIs, detects delay patterns, and produces AI-style operational insights.

## Features

- Synthetic transit data ingestion
- Delay detection
- KPI generation
- Route reliability scoring
- Time-based delay trends
- Pattern-based AI insights
- Recommended operational actions
- FastAPI API endpoints
- Dockerized backend environment

## Data Source

This prototype uses synthetic transit trip data located at:

`app/data/synthetic/transit_trips.csv`

No personally identifiable information (PII) is used.

## Run Backend with Docker

```powershell
cd backend
docker-compose up --buildj