from app.services.data_processor import load_transit_data

# ------------------------------------------------------------
# GLOBAL CACHE
# ------------------------------------------------------------
# This stores the computed analytics result in memory
# so we don’t recompute heavy GTFS data on every API call
_cached_analysis = None


def analyze_transit_data():
    """
    Main analytics engine for TransitWatch AI.

    This function:
    - Loads transit data (GTFS or synthetic)
    - Combines scheduled + actual trips
    - Computes system KPIs
    - Computes delay trends by hour
    - Computes route-level performance metrics

    Returns:
        Dictionary containing all analytics results
    """

    global _cached_analysis

    # ------------------------------------------------------------
    # CACHE CHECK (PERFORMANCE OPTIMIZATION)
    # ------------------------------------------------------------
    # If we already computed the analytics once,
    # return the cached result instead of recalculating
    if _cached_analysis is not None:
        return _cached_analysis

    # ------------------------------------------------------------
    # LOAD DATA
    # ------------------------------------------------------------
    # This pulls data from GTFS static files (or synthetic if switched)
    scheduled_trips, actual_trips = load_transit_data(source="synthetic")

    # ------------------------------------------------------------
    # MERGE SCHEDULED + ACTUAL DATA
    # ------------------------------------------------------------
    # Combine both datasets into a single unified structure
    trips = []

    for i in range(len(scheduled_trips)):
        trips.append({
            "route": scheduled_trips[i]["route"],
            "hour": scheduled_trips[i]["hour"],
            "scheduled_time": scheduled_trips[i]["scheduled_time"],
            "delay_minutes": actual_trips[i]["actual_delay"]
        })

    total_trips = len(trips)

    # ------------------------------------------------------------
    # EDGE CASE: NO DATA
    # ------------------------------------------------------------
    if total_trips == 0:
        _cached_analysis = {
            "total_trips": 0,
            "delayed_trips": 0,
            "on_time_trips": 0,
            "delay_by_hour": {},
            "route_summary": {},
            "raw_trips": []
        }
        return _cached_analysis

    # ------------------------------------------------------------
    # BASIC KPI CALCULATIONS
    # ------------------------------------------------------------
    delayed_trips = sum(
        1 for trip in trips if trip["delay_minutes"] > 0
    )

    on_time_trips = total_trips - delayed_trips

    # ------------------------------------------------------------
    # AGGREGATION STRUCTURES
    # ------------------------------------------------------------
    delay_by_hour = {}
    route_summary = {}

    # ------------------------------------------------------------
    # LOOP THROUGH TRIPS
    # ------------------------------------------------------------
    for trip in trips:
        hour = trip["hour"]
        route = trip["route"]
        delay = trip["delay_minutes"]

        # -------------------------
        # DELAY TREND BY HOUR
        # -------------------------
        delay_by_hour[hour] = delay_by_hour.get(hour, 0) + delay

        # -------------------------
        # ROUTE INITIALIZATION
        # -------------------------
        if route not in route_summary:
            route_summary[route] = {
                "total_trips": 0,
                "delayed_trips": 0,
                "total_delay_minutes": 0
            }

        # -------------------------
        # UPDATE ROUTE METRICS
        # -------------------------
        route_summary[route]["total_trips"] += 1
        route_summary[route]["total_delay_minutes"] += delay

        if delay > 0:
            route_summary[route]["delayed_trips"] += 1

    # ------------------------------------------------------------
    # COMPUTE ROUTE PERFORMANCE METRICS
    # ------------------------------------------------------------
    for route, data in route_summary.items():
        route_total = data["total_trips"]
        route_on_time = route_total - data["delayed_trips"]

        # Reliability = % of trips on time
        data["reliability_score"] = round(
            (route_on_time / route_total) * 100,
            2
        )

        # Average delay per trip
        data["average_delay_minutes"] = round(
            data["total_delay_minutes"] / route_total,
            2
        )

    # ------------------------------------------------------------
    # SORT HOURS (IMPORTANT FOR CLEAN UI GRAPH)
    # ------------------------------------------------------------
    hour_order = [
        "12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM",
        "6 AM", "7 AM", "8 AM", "9 AM", "10 AM", "11 AM",
        "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM",
        "6 PM", "7 PM", "8 PM", "9 PM", "10 PM", "11 PM"
    ]

    delay_by_hour = {
        hour: delay_by_hour[hour]
        for hour in hour_order
        if hour in delay_by_hour
    }

    # ------------------------------------------------------------
    # FINAL RESULT OBJECT
    # ------------------------------------------------------------
    _cached_analysis = {
        "total_trips": total_trips,
        "delayed_trips": delayed_trips,
        "on_time_trips": on_time_trips,
        "delay_by_hour": delay_by_hour,
        "route_summary": route_summary,
        "raw_trips": trips
    }

    return _cached_analysis