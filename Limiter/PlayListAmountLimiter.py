from Limiter.UserLimiter import UserLimiter


class PlayListAmountLimiter(UserLimiter):
    def __init__(self, user,limit):
        super().__init__(user)
        self.amount_limit = 5

    def limit(self):
        if len(self.user.playlists.keys()) > self.amount_limit:
            self.user.playlists = self.user.playlists[:self.amount_limit]
            PlayListAmountRestrictedException(
                f"you have a {self.user.type} user that is limited to {self.users_limits[self.user.type]} songs.")



class PlayListAmountRestrictedException(Exception):
    pass
