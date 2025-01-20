import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Метод {func.__name__} выполнен {elapsed_time:.4f} секунд")
        return result
    return wrapper

def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Метод  {func.__name__} вызван {wrapper.calls} раз")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper
