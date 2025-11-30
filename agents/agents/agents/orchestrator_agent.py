from typing import Dict, Any

from agents.travel_intent_agent import TravelIntentAgent
from agents.flights_agent import FlightsAgent
from agents.hotels_agent import HotelsAgent
from agents.activities_agent import ActivitiesAgent
from memory.session_service import SessionService
from evaluation.itinerary_eval import score_itinerary


class OrchestratorAgent:
    """
    Coordinates all agents and produces final travel plan.
    """

    def __init__(self):
        self.session = SessionService()
        self.intent_agent = TravelIntentAgent()
        self.flights_agent = FlightsAgent()
        self.hotels_agent = HotelsAgent()
        self.activities_agent = ActivitiesAgent()

    def run(self, user_input: str) -> Dict[str, Any]:
        # Step 1: parse intent
        intent = self.intent_agent.parse_request(user_input)
        self.session.save_intent(intent)

        # Step 2: get flights and hotels (parallelizable in real system)
        flights = self.flights_agent.get_flights(intent)
        hotels = self.hotels_agent.get_hotels(intent)

        # Step 3: build itinerary
        itinerary = self.activities_agent.build_itinerary(intent, flights, hotels)

        # Step 4: evaluate
        score = score_itinerary(itinerary)

        result = {
            "intent": intent,
            "flights": flights,
            "hotels": hotels,
            "itinerary": itinerary,
            "itinerary_score": score,
        }
        self.session.save_plan(result)
        return result
