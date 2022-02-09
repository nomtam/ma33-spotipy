import itertools


class LimitedSearcher:
    def __init__(self,data):
        self.limit = 5

    def limited_search(self, func, *args):
        def wrapper():
            return dict(itertools.islice(func(*args).items(), self.limit))

        return wrapper()
