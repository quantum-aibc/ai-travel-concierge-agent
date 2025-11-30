class SessionService:
    """
    Simple in-memory session store.
    In a real system this could be backed by Redis / DB.
    """

    def __init__(self):
        self._data = {}

    def save_intent(self, intent):
        self._data["intent"] = intent

    def save_plan(self, plan):
        self._data["plan"] = plan

    def get_session_data(self):
        return self._data
