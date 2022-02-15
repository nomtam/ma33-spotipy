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

# CR: in general would assume the Search method returns what you need so you can just return it to the user.
#  The need of extra logic in this class makes me understand that if I would like to change Search logic
#  I will need to access 2 places. That's not good
@app.route("/<user>/artists", methods=['GET'])
def get_all_artists(user):
    artists = Searcher(users[user], data).search(SearchingOptions.get_all_artists)
    # CR: jsonify
    return json.dumps(
        {artist.name: [album.name for a_id, album in artist.albums.items()] for artist in artists})


@app.route("/<user>/artist/<artist_id>/albums", methods=['GET'])
def get_artist_albums(user, artist_id):
    albums = Searcher(users[user], data).search(SearchingOptions.get_artist_albums, artist_id)
    # CR: jsonify
    return json.dumps(albums)


@app.route("/<user>/artist/<artist_id>/top_songs", methods=['GET'])
# CR: super coupled name without a need
def get_top10_songs(user, artist_id):
    songs = Searcher(users[user], data).search(SearchingOptions.get_top10_songs, artist_id)
    # CR: jsonify
    return json.dumps([song.__str__() for song in songs])


@app.route("/<user>/album/<album_id>", methods=['GET'])
def get_album_songs(user, album_id):
    songs = Searcher(users[user], data).search(SearchingOptions.get_album_songs, album_id)
    # CR: jsonify
    return json.dumps([song.__dict__ for song_id, song in songs.items()])


# CR: can be in if __name__ == '__main__':
def start_api():
    app.run()
