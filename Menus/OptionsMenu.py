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

user = PremiumUser("")


class OptionsMenu:
    def __init__(self, user):
        self.user = user

    def show_options_menu(self):
        options_menu = ConsoleMenu("spotipy-options")
        search_options = ConsoleMenu("search-options")
        data = Data()
        SongLoader(data).load_songs_in_directory(configuration.songs_path)
        search = SubmenuItem("search", search_options, options_menu)
        add_playlist = FunctionItem("add a playlist", add_new_playlist, (self.user, data))
        options_menu.append_item(search)
        options_menu.append_item(add_playlist)
        search_options.append_item(FunctionItem("get all artists", search_func, (self.user, data)))
        options_menu.show()


users = {
    'free': FreeUser,
    'premium': PremiumUser
}


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
