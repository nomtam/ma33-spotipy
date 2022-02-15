# CR: I think this shouldn't be a class. the limit can be solved much
#  easier in the User class with config and an extra method
class PlayListSizeLimiter:
    def __init__(self, size_limit):
        self.size_limit = size_limit

    def limit(self, playlist):
        if len(playlist.songs) > self.size_limit:
            raise RestrictedPlayListException(f"you are restricted to {self.limit} songs per playlist.")


# CR: exceptions should be in a dedicated class
class RestrictedPlayListException(Exception):
    pass
