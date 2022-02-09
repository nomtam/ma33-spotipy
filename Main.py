import configuration
from Application import Application
from Music.Data import Data
from PlayList.PlayList import PlayList
from Searcher.SearchingOptions import *
from Music.SongLoader import SongLoader
from User.FreeUser import FreeUser

data = Data()
loader = SongLoader(data)
loader.load_songs_in_directory(configuration.songs_path)
user = FreeUser('tomer')
app = Application(user, data)
playlist = list(data.songs.values())[:6]
user.add_playlist(PlayList('cool',playlist))
print(app.search(SearchingOptions.get_all_artists))
