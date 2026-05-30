from app.services.analytics_engine import analyze_transit_data


def generate_kpis():
    analytics = analyze_transit_data()

    total_trips = analytics["total_trips"]
    delayed_trips = analytics["delayed_trips"]
    on_time_trips = analytics["on_time_trips"]

    delay_frequency = round((delayed_trips / total_trips) * 100, 2)
    reliability_score = round((on_time_trips / total_trips) * 100, 2)

    delay_by_hour = analytics["delay_by_hour"]
    peak_disruption_time = max(delay_by_hour, key=delay_by_hour.get)

    return {
        "total_trips": total_trips,
        "delayed_trips": delayed_trips,
        "on_time_trips": on_time_trips,
        "delay_frequency_percent": delay_frequency,
        "peak_disruption_time": peak_disruption_time,
        "reliability_score": reliability_score,
        "delay_by_hour": delay_by_hour,
        "route_summary": analytics["route_summary"]
    }