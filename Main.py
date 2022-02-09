from Data import Data
from SongLoader import SongLoader
data = Data()
loader = SongLoader(data)
loader.load_songs_in_directory('Songs')
print(data)
