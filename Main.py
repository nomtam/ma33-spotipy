import configuration
from Application import Application
from Data import Data
from Searcher.Searcher import *
from SongLoader import SongLoader
from User.FreeUser import FreeUser

from User.PremiumUser import PremiumUser

data = Data()
loader = SongLoader(data)
loader.load_songs_in_directory(configuration.songs_path)
user = FreeUser('tomer')
app = Application(user, data)
print(app.searcher.limited_search(Searcher(data).get_all_artists))
