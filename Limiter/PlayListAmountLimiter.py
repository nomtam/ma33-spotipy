# CR: same like the second class
class PlayListAmountLimiter:
    def __init__(self, user, limit):
        self.amount_limit = limit
        self.user = user

    def limit(self):
        if len(self.user.playlists.keys()) > self.amount_limit:
            self.user.playlists = self.user.playlists[:self.amount_limit]
            PlayListAmountRestrictedException(
                f"you have a {self.user.type} user that is limited to {self.amount_limit} songs.")


# CR: same as all other exceptions
class PlayListAmountRestrictedException(Exception):
    pass
