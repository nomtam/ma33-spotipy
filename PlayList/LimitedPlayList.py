from PlayList.PlayList import PlayList


class LimitedPlayList(PlayList):
    def __init__(self, name, limit, songs={}):
        self.limit = limit
        if len(list(songs.keys())) > limit:
            raise RestrictedPlayListException(f"you are restricted to {limit} songs per playlist.")

    def add_song_to_playlist(self, song):
        if len(list(self.songs.keys())) >= self.limit:
            raise RestrictedPlayListException(f"you are restricted to {self.limit} songs per playlist.")
        else:
            super.add_song_to_playlist(self, song)


class RestrictedPlayListException(Exception):
    pass
