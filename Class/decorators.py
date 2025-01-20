import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Method {func.__name__} executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper

def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Method {func.__name__} called {wrapper.calls} times")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper
