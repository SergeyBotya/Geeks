def type_logger(func):

    def wrapped_func(*args):
        for arg in args:
            print(f'{arg}: {type(arg)}')
    return wrapped_func


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5, 8, 13)
