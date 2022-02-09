class SearchingOptions:
    @staticmethod
    def get_all_artists(data):
        r = data.artists
        return data.artists

    @staticmethod
    def get_artist_songs(data, artist_id):
        albums = data.artists[artist_id].albums.values()
        return [album.name for album in albums]

    @staticmethod
    def get_top10_songs(data, artist_id):
        albums = list(data.artists[artist_id].albums.values())
        artist_songs = []
        for album in albums:
            for song in list(album.songs.values()):
                artist_songs.append(song)
        return list(sorted(artist_songs, key=lambda song: song.popularity, reverse=True))[:10]

    @staticmethod
    def get_album_songs(data, album_id):
        return data.albums[album_id].songs
