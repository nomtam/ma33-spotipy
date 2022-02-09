class Song:

    def __init__(self, unique_id, name, popularity):
        self.unique_id = unique_id
        self.name = name
        self.popularity = popularity

    def __str__(self):
        return f"name: {self.name}"
