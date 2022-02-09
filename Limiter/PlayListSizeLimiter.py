class PlayListSizeLimiter:
    def __init__(self, size_limit):
        self.size_limit = size_limit

    def limit(self, playlist):
        if len(playlist.songs) > self.size_limit:
            raise RestrictedPlayListException(f"you are restricted to {self.limit} songs per playlist.")


class RestrictedPlayListException(Exception):
    pass
