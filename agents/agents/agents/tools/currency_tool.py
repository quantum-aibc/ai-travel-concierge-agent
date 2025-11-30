class CurrencyTool:
    """
    Mock currency converter.
    In a real implementation this would use an FX API.
    """

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        if from_currency == to_currency:
            return amount
        # Very naive mock conversion
        rate = 1.0
        if to_currency == "EUR":
            rate = 0.9
        if to_currency == "INR":
            rate = 80.0
        return amount * rate
