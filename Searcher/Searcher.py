# CR: bad naming.
class Searcher:
    def __init__(self, user, data):
        self.user = user
        self.data = data
        self.searcher = self.user.searcher

    # CR: spacing missing
    # CR: really weird design pattern. Why do you use this method and not just access the inner methods.
    #  Using it like these and with *args makes it prone to error
    def search(self, searching_option,*args):
        return self.searcher.search(searching_option,self.data,*args)

