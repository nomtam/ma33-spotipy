from User.PremiumUser import PremiumUser


class Artist(PremiumUser):
    def __init__(self, unique_id, name, albums, playlists ={}):
        super().__init__(name, playlists)
        self.unique_id = unique_id
        self.name = name
        self.albums = albums

    def __str__(self):
        return f"name: {self.name} , albums: {self.albums}"
