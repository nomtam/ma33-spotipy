from Song import Song


class Album:
    def __init__(self, unique_id, name, songs):
        self.name = name
        self.unique_id = unique_id
        self.songs = songs
