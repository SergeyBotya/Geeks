def val_checker(x):
    def _val(func):
        def wrapped_func(*args):
            for arg in args:
                if arg > 0:
                    result = func(*args)
                    print(result)
                else:
                    print(f"ValueError: wrong val {arg}")
        return wrapped_func
    return _val


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(-5)