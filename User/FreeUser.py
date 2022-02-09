import logging

from Limiter.PlayListAmountLimiter import PlayListAmountLimiter
from PlayList.LimitedPlayList import LimitedPlayList, RestrictedPlayListException
from PlayList.PlayList import PlayList
from Searcher.LimitedSearcher import LimitedSearcher
from User.PremiumUser import PremiumUser


class FreeUser(PremiumUser):
    def __init__(self, user_name, playlists={}):
        super().__init__(user_name, playlists)
        self.searcher = LimitedSearcher
        if not all(isinstance(playlist, LimitedPlayList) for playlist in list(playlists.values())):
            raise RestrictedPlayListException("you gave one or more playlists with too much songs for a free user.")
        PlayListAmountLimiter(self,5).limit()

    def add_playlist(self, playlist: PlayList):
        if not isinstance(playlist, LimitedPlayList):
            raise RestrictedPlayListException("the playlist has too much songs for a free user.")
        super().add_playlist(playlist)
        PlayListAmountLimiter(self,5).limit()
