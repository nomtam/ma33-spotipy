class Data:
    def __init__(self):
        self.artists = {}
        self.albums = {}
        self.songs = {}

    def __str__(self):
        # CR: why?
        return f"artists:\n{self.artists}\nalbums:\n{self.albums}\nsongs:\n{self.songs}"
