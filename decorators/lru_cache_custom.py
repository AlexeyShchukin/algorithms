from collections import OrderedDict
from functools import wraps


def lru_cache_custom(max_size=10):
    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args + tuple(sorted(kwargs.items()))
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            cache.move_to_end(key)

            if len(cache) > max_size:
                cache.popitem(last=False)

            return result

        return wrapper

    return decorator
