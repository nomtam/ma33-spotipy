from Song import Song


class Album:
    def __init__(self, unique_id,songs: list(Song)):
        self.unique_id = unique_id
        self.songs = songs
