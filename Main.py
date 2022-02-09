import configuration
from Data import Data
from SongLoader import SongLoader
data = Data()
loader = SongLoader(data)
loader.load_songs_in_directory(configuration.songs_path)
for artist in data.artists.values():
    print(artist)
