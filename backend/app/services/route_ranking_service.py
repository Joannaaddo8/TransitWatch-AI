def get_top_worst_routes(analysis, limit=5):
    route_summary = analysis["route_summary"]

    ranked = sorted(
        route_summary.items(),
        key=lambda item: item[1]["reliability_score"]
    )

    worst_routes = ranked[:limit]

    result = []

    for route, data in worst_routes:
        result.append({
            "route": f"Route {route}",
            "reliability_score": data["reliability_score"],
            "average_delay_minutes": data["average_delay_minutes"],
            "total_trips": data["total_trips"]
        })

    return result