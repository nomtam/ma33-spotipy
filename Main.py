import configuration
from LoginMenu import LoginMenu
from Music.Data import Data
from PlayList.PlayList import PlayList
from Searcher.Searcher import *
from Music.SongLoader import SongLoader
from Searcher.SearchingOptions import SearchingOptions
from User.FreeUser import FreeUser
from User.UsersSystem import UsersSystem

data = Data()
loader = SongLoader(data)
loader.load_songs_in_directory(configuration.songs_path)
user = FreeUser('tomer')
system = UsersSystem()
LoginMenu().show_login_menu()
