import itertools


class LimitedSearcher:
    @staticmethod
    def search(func, *args):
        def wrapper():
            r = dict(itertools.islice(func(*args).items(), 5))
            return dict(itertools.islice(func(*args).items(), 5))

        return wrapper()
