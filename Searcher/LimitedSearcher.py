import itertools


class LimitedSearcher:
    @staticmethod
    def search(func, *args):
        def wrapper():
            return dict(itertools.islice(func(*args).items(), 5))

        return wrapper()
