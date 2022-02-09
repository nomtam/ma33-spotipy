from PlayList import PlayList


class User:
    def __init__(self, playlists={}):
        self.playlists = playlists

    def add_playlist(self, playlist: PlayList):
        if playlist.name in self.playlists.keys():
            raise PlayListExistsException("this playlist's name is taken")
        else:
            self.playlists[playlist.name] = playlist


class PlayListExistsException(Exception):
    pass
