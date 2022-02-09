class Searcher:
    def __init__(self, data):
        self.data = data

    def get_all_artists(self):
        return self.data.artists

    def get_artist_songs(self, artist_id):
        albums = self.data.artists[artist_id].albums.values()
        return [album.name for album in albums]

    def get_top10_songs(self, artist_id):
        albums = list(self.data.artists[artist_id].albums.values())
        artist_songs = []
        for album in albums:
            for song in list(album.songs.values()):
                artist_songs.append(song)
        return list(sorted(artist_songs, key=lambda song: song.popularity, reverse=True))[:10]

    def get_album_songs(self, album_id):
        return self.data.albums[album_id].songs
{}