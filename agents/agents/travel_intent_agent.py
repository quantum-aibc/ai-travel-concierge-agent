from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TravelIntent:
    destination: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    budget: Optional[float] = None
    currency: str = "USD"
    travelers_count: int = 1
    travel_style: str = "mixed"  # budget / luxury / business / family / mixed
    interests: List[str] = None


class TravelIntentAgent:
    """
    Parses a free-form user request into a structured TravelIntent.
    In a real implementation this would call an LLM (e.g. Gemini).
    """

    def __init__(self, llm_client=None):
        self.llm_client = llm_client

    def parse_request(self, user_input: str) -> TravelIntent:
        # TODO: Replace this simple heuristic with an LLM-powered parser
        # For now, just a mocked example
        destination = "Japan" if "japan" in user_input.lower() else "Unknown"
        budget = 1200.0 if "1200" in user_input else None
        interests = []

        for word in ["food", "anime", "culture", "nature", "shopping"]:
            if word in user_input.lower():
                interests.append(word)

        return TravelIntent(
            destination=destination,
            budget=budget,
            interests=interests or ["general"],
        )
