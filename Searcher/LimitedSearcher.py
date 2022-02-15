import itertools


# CR: hard codded to 5
# CR: why do you need this? Search regularly and return top 5
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
