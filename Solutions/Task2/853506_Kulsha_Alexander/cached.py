def cached(func_to_decorate):
    cache = {}

    def wrapper(*args, **kwargs):
        if args in cache:
            print("cached")
            return cache[args]
        else:
            print("caching...")
            value = func_to_decorate(*args, **kwargs)
            cache[args] = value
            return value

    return wrapper
