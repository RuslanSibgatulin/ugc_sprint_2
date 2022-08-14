from functools import wraps
from time import time


def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time()
        func_name = func.__name__
        print(f"Function {func_name} started.")
        result = func(*args, **kwargs)
        end = time()
        print(f"Function {func_name} finished. \nExcecute time: {round(end-start, 3)} sec.")
        return result
    return inner
