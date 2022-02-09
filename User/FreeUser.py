import logging

from Limiter.PlayListAmountLimiter import PlayListAmountLimiter
from Limiter.PlayListSizeLimiter import PlayListSizeLimiter
from PlayList.LimitedPlayList import LimitedPlayList, RestrictedPlayListException
from PlayList.PlayList import PlayList
from Searcher.LimitedSearcher import LimitedSearcher
from User.PremiumUser import PremiumUser


class FreeUser(PremiumUser):
    def __init__(self, user_name, playlists={}):
        super().__init__(user_name, playlists)
        self.searcher = LimitedSearcher
        for playlist in playlists:
            PlayListSizeLimiter(20).limit(playlist)
        PlayListAmountLimiter(self, 5).limit()

    def add_playlist(self, playlist: PlayList):
        PlayListSizeLimiter(20).limit(playlist)
        super().add_playlist(playlist)
        PlayListAmountLimiter(self, 5).limit()
