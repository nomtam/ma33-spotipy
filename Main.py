import configuration
from Menus.LoginMenu import LoginMenu
from Music.Data import Data
from Music.SongLoader import SongLoader
from User.FreeUser import FreeUser
from User.UsersSystem import UsersSystem

data = Data()
loader = SongLoader(data)
loader.load_songs_in_directory(configuration.songs_path)
user = FreeUser('tomer')
system = UsersSystem()
LoginMenu().show_login_menu()
