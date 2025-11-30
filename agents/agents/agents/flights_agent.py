from typing import List, Dict
from tools.currency_tool import CurrencyTool


class FlightsAgent:
    """
    Responsible for finding flight / transport options.
    In this skeleton, we return mock data.
    """

    def __init__(self, currency_tool: CurrencyTool | None = None):
        self.currency_tool = currency_tool or CurrencyTool()

    def get_flights(self, intent) -> List[Dict]:
        # TODO: integrate with search APIs or ADK tools
        base_price_usd = 650.0
        price = self.currency_tool.convert(
            amount=base_price_usd, from_currency="USD", to_currency=intent.currency
        )

        return [
            {
                "from": "Home City",
                "to": intent.destination,
                "airline": "Example Air",
                "duration_hours": 10,
                "stops": 1,
                "price": price,
                "currency": intent.currency,
            }
        ]
