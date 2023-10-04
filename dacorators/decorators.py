# function and class decorator
import functools


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start wrapper")
        result: int = func(*args, **kwargs)
        print("end wrapper with result", result)
        return result

    return wrapper


@start_end_decorator
def print_name(par: int):
    print("Pradeep + ", par)
    return par * 2


print(help(print_name))
print(print_name.__name__)

# print_name = start_end_decorator(print_name)
print_name(10)
