# TransitWatch AI

TransitWatch AI is an intelligent transit analytics platform developed for the Transit Data Challenge 2026.

## Features

- GTFS Static Integration
- GTFS Realtime Vehicle Tracking
- Route Performance Ranking
- Reliability Analytics
- Delay Frequency Analysis
- AI-Powered Operational Insights
- CrewAI Multi-Agent Recommendations
- Interactive Transit Dashboard

## Technology Stack

### Backend
- FastAPI
- Python
- Pandas
- CrewAI
- Mistral LLM

### Frontend
- React
- Vite
- Axios

## Running Locally

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on:

```text
http://localhost:8001
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

## Data Sources

- GTFS Static
- GTFS Realtime
- Synthetic Transit Operations Dataset

## Project Structure

```text
backend/
frontend/
```

## Authors

Joan Addo

Transit Data Challenge 2026