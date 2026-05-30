# ------------------------------------------------------------
# ROUTE FORMATTER
# ------------------------------------------------------------
# Converts raw GTFS route values like "5" or "501"
# into user-friendly labels like "Route 5" or "Route 501"
def format_route(route):
    return f"Route {route}"


# ------------------------------------------------------------
# DELAY TIME FORMATTER
# ------------------------------------------------------------
# Converts large minute values into readable time.
# Example:
# 13804 minutes → 230 hours 4 minutes
def format_delay_time(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60

    if hours == 0:
        return f"{remaining_minutes} minutes"

    return f"{hours:,} hours {remaining_minutes} minutes"

def classify_reliability(score):
    if score < 50:
        return "Low reliability"
    elif score < 80:
        return "Moderate reliability"
    return "Good reliability"


# ------------------------------------------------------------
# MAIN INSIGHTS ENGINE
# ------------------------------------------------------------
def generate_insights(analysis):
    """
    Generates AI-style operational insights from analytics results.

    This function uses the analytics output to:
    - Detect peak disruption time
    - Identify the worst-performing routes
    - Identify a best-performing route
    - Recommend a practical service improvement
    """

    route_summary = analysis["route_summary"]
    delay_by_hour = analysis["delay_by_hour"]

    insights = []

    # ------------------------------------------------------------
    # 1. PEAK DISRUPTION DETECTION
    # ------------------------------------------------------------
    peak_hour = max(delay_by_hour, key=delay_by_hour.get)
    peak_delay = delay_by_hour[peak_hour]

    insights.append({
        "title": "Peak Disruption",
        "message": f"Peak disruption occurs around {peak_hour}.",
        "explanation": (
            f"Total delay reaches {format_delay_time(peak_delay)} during this hour, "
            "indicating the highest congestion period."
        )
    })

    # ------------------------------------------------------------
    # 2. WORST ROUTE DETECTION
    # ------------------------------------------------------------
    sorted_routes = sorted(
        route_summary.items(),
        key=lambda item: item[1]["reliability_score"]
    )

    worst_routes = sorted_routes[:3]

    for route, data in worst_routes:
        insights.append({
            "title": f"{format_route(route)} Performance",
            "message": (
                f"Reliability: {data['reliability_score']}% | "
                f"Avg Delay: {data['average_delay_minutes']} mins"
            ),
            "explanation": (
                f"{classify_reliability(data['reliability_score'])} — "
                "monitor peak periods and service pressure on this route."
            )
        })

    # ------------------------------------------------------------
    # 3. BEST ROUTE DETECTION
    # ------------------------------------------------------------
    best_route, best_data = sorted_routes[-1]

    # Only add best route if it's NOT already in worst_routes
    if best_route not in [r for r, _ in worst_routes]:
       insights.append({
          "title": f"{format_route(best_route)} Performance",
          "message": (
              f"Reliability: {best_data['reliability_score']}% | "
              f"Avg Delay: {best_data['average_delay_minutes']} mins"
            ),
            "explanation": "This route is operating efficiently and can be used as a performance benchmark."
    })

    # ------------------------------------------------------------
    # 4. RECOMMENDATION ENGINE
    # ------------------------------------------------------------
    worst_route, worst_data = worst_routes[0]

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
            "Increase overall system reliability"
        ]
    })

    return insights