import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

load_dotenv()

LLM_MODEL = os.getenv(
    "MISTRAL_MODEL_NAME",
    "mistral-large-latest"
)


def generate_crew_ai_summary(analysis):
    route_summary = analysis.get("route_summary", {})
    delay_by_hour = analysis.get("delay_by_hour", {})

    total_trips = analysis.get("total_trips", 0)
    delayed_trips = analysis.get("delayed_trips", 0)
    on_time_trips = analysis.get("on_time_trips", 0)

    delay_frequency = round((delayed_trips / total_trips) * 100, 2) if total_trips else 0
    reliability_score = round((on_time_trips / total_trips) * 100, 2) if total_trips else 0

    worst_routes = sorted(
        route_summary.items(),
        key=lambda item: item[1]["reliability_score"]
    )[:3]

    peak_hour = max(delay_by_hour, key=delay_by_hour.get) if delay_by_hour else "N/A"

    analytics_context = f"""
    Total trips analyzed: {total_trips}
    Delayed trips: {delayed_trips}
    On-time trips: {on_time_trips}
    Reliability score: {reliability_score}%
    Delay frequency: {delay_frequency}%
    Peak disruption hour: {peak_hour}
    Worst-performing routes: {worst_routes}
    """

    try:
        transit_analyst = Agent(
            role="Transit Analyst Agent",
            goal="Analyze transit reliability and recommend operational improvements.",
            backstory="You are an experienced public transit operations analyst.",
            llm=LLM_MODEL,
            verbose=False,
        )

        analysis_task = Task(
            description=f"""
            Analyze the following TransitWatch AI performance data.

            {analytics_context}

            Produce a concise operational summary for TTC-style transit managers.
            Focus on reliability, peak disruption, route risk, and one practical recommendation.
            """,
            expected_output="A concise 3-5 sentence transit operations summary with one actionable recommendation.",
            agent=transit_analyst,
        )

        crew = Crew(
            agents=[transit_analyst],
            tasks=[analysis_task],
            verbose=False,
        )

        result = crew.kickoff()

        return {
            "title": "CrewAI Multi-Agent Operational Summary",
            "framework": "CrewAI with Mistral LLM",
            "model": LLM_MODEL,
            "agents": [
                "Transit Analyst Agent"
            ],
            "metrics": {
                "total_trips": total_trips,
                "delayed_trips": delayed_trips,
                "on_time_trips": on_time_trips,
                "reliability_score": reliability_score,
                "delay_frequency_percent": delay_frequency,
                "peak_disruption_hour": peak_hour,
            },
            "summary": str(result),
        }

    except Exception as error:
        return {
            "title": "CrewAI Multi-Agent Operational Summary",
            "framework": "CrewAI fallback mode",
            "model": LLM_MODEL,
            "agents": [
                "Transit Analyst Agent"
            ],
            "metrics": {
                "total_trips": total_trips,
                "delayed_trips": delayed_trips,
                "on_time_trips": on_time_trips,
                "reliability_score": reliability_score,
                "delay_frequency_percent": delay_frequency,
                "peak_disruption_hour": peak_hour,
            },
            "summary": (
                f"TransitWatch AI analyzed {total_trips} trips with a reliability score of "
                f"{reliability_score}% and a delay frequency of {delay_frequency}%. "
                f"The highest disruption occurs around {peak_hour}. "
                f"Recommended action: monitor peak periods and prioritize lower-performing routes."
            ),
            "error": str(error),
        }