def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} called with {args}")
        return func(*args)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg**2 for arg in args]


addition = add(4, 5)
print(addition)

squared = square_all(3, 45, 5)
print(squared)