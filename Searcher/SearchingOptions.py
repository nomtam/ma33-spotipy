# CR: class Search
class SearchingOptions:
    @staticmethod
    def get_all_artists(data):
        return list(data.artists.values())

    @staticmethod
    def get_artist_albums(data, artist_id):
        albums = data.artists[artist_id].albums.values()
        return [album.name for album in albums]

    @staticmethod
    # CR: why 10? so coupled... Get it in config or as a var to method
    def get_top10_songs(data, artist_id):
        albums = list(data.artists[artist_id].albums.values())
        artist_songs = []
        for album in albums:
            # CR: do you have to use list()
            for song in list(album.songs.values()):
                artist_songs.append(song)
                # CR: shadowing name from outer scope. Realy bad practice
                # CR: :10 is hard codded
        return list(sorted(artist_songs, key=lambda song: song.popularity, reverse=True))[:10]

    @staticmethod
    def get_album_songs(data, album_id):
        return data.albums[album_id].songs
