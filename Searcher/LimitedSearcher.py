import itertools


class LimitedSearcher:
    @staticmethod
    def search(func, *args):
        def wrapper():
            result = func(*args)
            if type(result) == dict:
                return dict(itertools.islice(func(*args).items(), 5))
            else:
                return list(result)[:5]

        return wrapper()
