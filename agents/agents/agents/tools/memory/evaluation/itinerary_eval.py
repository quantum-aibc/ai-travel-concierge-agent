from typing import List, Dict


def score_itinerary(itinerary: List[Dict]) -> float:
    """
    Very simple scoring based on number of days and activities.
    In a real system this would consider distances, times, and user constraints.
    """
    if not itinerary:
        return 0.0

    days = len(itinerary)
    total_activities = sum(len(day.get("activities", [])) for day in itinerary)
    return round(days * 1.0 + total_activities * 0.5, 2)
