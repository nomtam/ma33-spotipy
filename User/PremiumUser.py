from Loggs.Logger import Logger
from PlayList.PlayList import PlayList
from Searcher.RegularSearcher import RegularSearcher


class PremiumUser:
    # CR: replace with =None and if not None
    def __init__(self, user_name, playlists={}):
        self.playlists = playlists
        self.user_name = user_name
        self.searcher = RegularSearcher
        # CR: why not ENUM?
        self.type = 'premium'

    def add_playlist(self, playlist: PlayList):
        if playlist.name in self.playlists.keys():
            # CR: why does the free text important?
            raise PlayListExistsException("this playlist's name is taken")
        else:
            self.playlists[playlist.name] = playlist
        Logger.logger.info(f"added the {playlist.name} playlist to user:{self.user_name} successfully ")


# CR: why are exceptions here
class PlayListExistsException(Exception):
    pass


class RestrictedUser(Exception):
    pass
