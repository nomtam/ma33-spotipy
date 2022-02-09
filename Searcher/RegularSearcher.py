class RegularSearcher:
    @staticmethod
    def search(func, *args):
        def wrapper():
            return func(*args)

        return wrapper()
