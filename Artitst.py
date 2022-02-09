class Artist:
    def __init__(self, unique_id, name, albums):
        self.unique_id = unique_id
        self.name = name
        self.albums = albums

    def __str__(self):
        return f"name: {self.name} , albums: {self.albums}"
