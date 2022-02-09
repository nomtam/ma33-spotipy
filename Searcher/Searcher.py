
class Searcher:
    def __init__(self, user, data):
        self.user = user
        self.data = data
        self.searcher = self.user.searcher

    def search(self, searching_option,*args):
        return self.searcher.search(searching_option,self.data,*args)

