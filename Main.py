import configuration
from Data import Data
from Searcher import Searcher
from SongLoader import SongLoader

data = Data()
loader = SongLoader(data)
loader.load_songs_in_directory(configuration.songs_path)
searcher = Searcher(data)
