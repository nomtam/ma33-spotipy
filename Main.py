import configuration
from Application import Application
from Data import Data
from Searcher.SearchingOptions import *
from SongLoader import SongLoader
from User.FreeUser import FreeUser

from User.PremiumUser import PremiumUser

data = Data()
loader = SongLoader(data)
loader.load_songs_in_directory(configuration.songs_path)
user = FreeUser('tomer')
app = Application(user, data)
print(app.search(SearchingOptions.get_all_artists))
