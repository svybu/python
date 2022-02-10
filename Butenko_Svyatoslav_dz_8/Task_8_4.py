def val_checker(predicate):
    def wrapper(func):
        def wrap(arg):
            if not predicate(arg):
                msg = 'wrong val ', arg
                raise ValueError(msg)
            return func(arg)
        return wrap
    return wrapper

@val_checker(lambda x:x >0 )
def calc_cube(x):
    return x**3

print(calc_cube(-5))