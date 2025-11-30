class DistanceTool:
    """
    Mock distance / travel time estimation tool.
    In a real implementation, this might call a Maps API.
    """

    def estimate_distance(self, origin: str, destination: str) -> float:
        # TODO: plug in real logic
        return 3.5  # km, mock value
