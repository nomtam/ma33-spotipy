from consolemenu import *
from consolemenu.items import *
import consolemenu

import configuration
from Music.Data import Data
from Music.SongLoader import SongLoader
from PlayList.PlayList import PlayList
from Searcher.Searcher import Searcher
from Searcher.SearchingOptions import SearchingOptions
from User.FreeUser import FreeUser
from User.PremiumUser import PremiumUser

preset_user = PremiumUser("")
def get_user(user, options_menu):
    global preset_user
    user_name = input("enter user name")
    options_menu.show()
    preset_user = user(user_name)


def add_new_playlist(user, data):
    playlist = PlayList(input("enter playlist name:"))
    print("enter s when you want to stop entering new songs")
    ans = input("enter song id: ")
    while ans != "s":
        song = data.songs[ans]
        playlist.add_song_to_playlist(song)
        ans = input("enter song id: ")
    user.add_playlist(playlist)


def search_func(preset_user, data):
    searcher = Searcher(preset_user, data)
    res = searcher.search(SearchingOptions.get_all_artists)
    print(res)


user_menu = ConsoleMenu("spotipy-login")
options_menu = ConsoleMenu("options")
search_options = ConsoleMenu("search-options")
data = Data()
SongLoader(data).load_songs_in_directory(configuration.songs_path)
free_user = FunctionItem("Free User", get_user, (FreeUser, options_menu))
premium_user = FunctionItem("Premium User", get_user, (PremiumUser, options_menu))
user_menu.append_item(free_user)
user_menu.append_item(premium_user)

search = SubmenuItem("search", search_options, options_menu)
add_playlist = FunctionItem("add a playlist", add_new_playlist, (preset_user, data))
options_menu.append_item(search)
options_menu.append_item(add_playlist)

search_options.append_item(FunctionItem("get all artists", search_func, (preset_user, data)))

user_menu.show()
