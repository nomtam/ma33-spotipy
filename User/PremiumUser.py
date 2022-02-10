from Loggs.Logger import Logger
from PlayList.PlayList import PlayList
from Searcher.RegularSearcher import RegularSearcher


class PremiumUser:
    def __init__(self, user_name, playlists={}):
        self.playlists = playlists
        self.user_name = user_name
        self.searcher = RegularSearcher

    def add_playlist(self, playlist: PlayList):
        if playlist.name in self.playlists.keys():
            raise PlayListExistsException("this playlist's name is taken")
        else:
            self.playlists[playlist.name] = playlist
        Logger.logger.info(f"added the {playlist.name} playlist to user:{self.user_name} successfully ")


class PlayListExistsException(Exception):
    pass


class RestrictedUser(Exception):
    pass
