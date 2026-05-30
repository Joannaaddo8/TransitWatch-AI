def format_route(route):
    return f"Route {route}"


def generate_insights(analytics):
    route_summary = analytics["route_summary"]
    delay_by_hour = analytics["delay_by_hour"]

    insights = []

    peak_hour = max(delay_by_hour, key=delay_by_hour.get)
    peak_delay = delay_by_hour[peak_hour]

    insights.append({
        "title": "Peak Disruption",
        "message": f"Peak disruption occurs around {peak_hour}.",
        "explanation": (
            f"Total delay reaches {peak_delay} minutes during this hour, "
            "indicating the highest congestion period."
        ),
    })

    worst_route = None
    lowest_score = 100

    for route, data in route_summary.items():
        reliability = data["reliability_score"]
        avg_delay = data["average_delay_minutes"]

        if reliability < lowest_score:
            lowest_score = reliability
            worst_route = route

        insights.append({
            "title": f"{format_route(route)} Performance",
            "message": f"Reliability: {reliability}% | Avg Delay: {avg_delay} mins",
            "explanation": (
                "Low reliability indicates frequent delays."
                if reliability < 50 else
                "Moderate reliability — monitor peak periods and service pressure on this route."
                if reliability < 80 else
                "This route is operating efficiently."
            ),
        })

    insights.append({
        "title": "Recommended Action",
        "message": f"Increase service frequency on {format_route(worst_route)} during {peak_hour}.",
        "explanation": (
            f"{format_route(worst_route)} has the lowest reliability and delays peak at "
            f"{peak_hour}, indicating demand may exceed current service capacity."
        ),
        "impact": [
            "Reduce passenger wait times",
            "Improve schedule adherence",
            "Increase overall system reliability",
        ],
    })

    return insights