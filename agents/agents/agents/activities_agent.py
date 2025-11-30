from typing import List, Dict


class ActivitiesAgent:
    """
    Creates a day-wise itinerary.
    This skeleton returns a simple mock itinerary.
    """

    def __init__(self):
        pass

    def build_itinerary(self, intent, flights, hotels) -> List[Dict]:
        # TODO: use search, weather & distance tools + loops
        days = 4
        itinerary = []
        for day in range(1, days + 1):
            itinerary.append(
                {
                    "day": day,
                    "summary": f"Explore {intent.destination} - Day {day}",
                    "activities": [
                        {
                            "name": "City walking tour",
                            "type": "culture",
                            "time": "09:00 - 12:00",
                        },
                        {
                            "name": "Local food experience",
                            "type": "food",
                            "time": "13:00 - 15:00",
                        },
                        {
                            "name": "Evening market visit",
                            "type": "shopping",
                            "time": "17:00 - 20:00",
                        },
                    ],
                }
            )
        return itinerary
