class MemoryBank:
    """
    Long-term memory for user preferences.
    Here it's a simple in-memory structure; in production it would be persistent.
    """

    def __init__(self):
        self.preferences = {}

    def update_preferences(self, user_id: str, key: str, value):
        user_pref = self.preferences.setdefault(user_id, {})
        user_pref[key] = value

    def get_preferences(self, user_id: str):
        return self.preferences.get(user_id, {})
