class Application:
    def __init__(self,user,data):
        self.user = user
        self.searcher = self.user.searcher(data)
