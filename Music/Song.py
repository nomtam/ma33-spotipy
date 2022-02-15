class Song:

    def __init__(self, unique_id, name, popularity):
        self.unique_id = unique_id
        self.name = name
        self.popularity = popularity

    def __str__(self):
        # CR: why?
        return f"name: {self.name} - popularity: {self.popularity}"
