from typing import List, Dict
from tools.distance_tool import DistanceTool


class HotelsAgent:
    """
    Suggests hotel / stay options based on budget & location.
    Currently returns mocked options.
    """

    def __init__(self, distance_tool: DistanceTool | None = None):
        self.distance_tool = distance_tool or DistanceTool()

    def get_hotels(self, intent) -> List[Dict]:
        # TODO: use search + real data
        avg_distance_km = self.distance_tool.estimate_distance("city_center", "hotel_1")

        nightly_rate = (intent.budget or 1000) / 4  # silly heuristic

        return [
            {
                "name": "Central Comfort Hotel",
                "area": "City Center",
                "nightly_rate": round(nightly_rate, 2),
                "currency": intent.currency,
                "distance_to_center_km": avg_distance_km,
                "rating": 4.3,
            }
        ]
