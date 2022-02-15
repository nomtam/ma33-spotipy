from Limiter.PlayListAmountLimiter import PlayListAmountLimiter
from Limiter.PlayListSizeLimiter import PlayListSizeLimiter
from PlayList.PlayList import PlayList
from Searcher.LimitedSearcher import LimitedSearcher
from User.PremiumUser import PremiumUser


# CR: why does this use PremiumUser? Best practice is to create User and two classes that use it
class FreeUser(PremiumUser):
    # CR: same as in free user
    def __init__(self, user_name, playlists={}):
        super().__init__(user_name, playlists)
        self.searcher = LimitedSearcher
        # CR: same. ENUM
        self.type = 'free'
        for playlist in playlists:
            # CR: weird implementation of limit. Why not just use an "if" and add the numbers in a config?
            PlayListSizeLimiter(20).limit(playlist)
        PlayListAmountLimiter(self, 5).limit()

    def add_playlist(self, playlist: PlayList):
        # CR: same as above
        PlayListSizeLimiter(20).limit(playlist)
        super().add_playlist(playlist)
        PlayListAmountLimiter(self, 5).limit()
