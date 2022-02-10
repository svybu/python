def type_logger(func):
    def wrapper(*args):
        for i in args:
            res = type(i)
            print(f'{i}: {res}')
    return wrapper

@type_logger
def calc_cube(*args):
    return args**3

calc_cube(1000, 2000, 50, 'xa')