class PlayList:
    def __init__(self, name, songs={}):
        self.name = name
        self.songs = songs

    def add_song_to_playlist(self, song):
        self.songs[song.unique_id] = song
