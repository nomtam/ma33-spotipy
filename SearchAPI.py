import json

from flask import Flask

import configuration
from Music.Data import Data
from Music.SongLoader import SongLoader
from Searcher.Searcher import Searcher
from Searcher.SearchingOptions import SearchingOptions
from User.FreeUser import FreeUser
from User.PremiumUser import PremiumUser

app = Flask(__name__)
data = Data()
loader = SongLoader(data)
loader.load_songs_in_directory(configuration.songs_path)

users = {
    "free": FreeUser(""),
    "premium": PremiumUser("")
}


@app.route("/<user>/artists", methods=['GET'])
def get_all_artists(user):
    artists = Searcher(users[user], data).search(SearchingOptions.get_all_artists)
    return json.dumps(
        {artist.name: [album.name for a_id, album in artist.albums.items()] for artist in artists})


@app.route("/<user>/artist/<artist_id>/albums", methods=['GET'])
def get_artist_albums(user, artist_id):
    albums = Searcher(users[user], data).search(SearchingOptions.get_artist_albums, artist_id)
    return json.dumps(albums)


@app.route("/<user>/artist/<artist_id>/top_songs", methods=['GET'])
def get_top10_songs(user, artist_id):
    songs = Searcher(users[user], data).search(SearchingOptions.get_top10_songs, artist_id)
    return json.dumps([song.__str__() for song in songs])


@app.route("/<user>/album/<album_id>", methods=['GET'])
def get_album_songs(user, album_id):
    songs = Searcher(users[user], data).search(SearchingOptions.get_album_songs, album_id)
    return json.dumps([song.__dict__ for song_id, song in songs.items()])


app.run()
