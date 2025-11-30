class WeatherTool:
    """
    Mock weather lookup tool.
    """

    def get_weather_summary(self, destination: str, month: str) -> str:
        # TODO: real weather API
        return f"Typical weather in {destination} in {month}: mild, occasional rain."
