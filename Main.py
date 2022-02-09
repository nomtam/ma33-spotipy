import configuration
from Music.Data import Data
from PlayList.PlayList import PlayList
from Searcher.Searcher import *
from Music.SongLoader import SongLoader
from Searcher.SearchingOptions import SearchingOptions
from User.FreeUser import FreeUser

data = Data()
loader = SongLoader(data)
loader.load_songs_in_directory(configuration.songs_path)
user = FreeUser('tomer')
searcher = Searcher(user, data)
playlist = list(data.songs.values())[:6]
user.add_playlist(PlayList('cool',playlist))
print(searcher.search(SearchingOptions.get_all_artists))
