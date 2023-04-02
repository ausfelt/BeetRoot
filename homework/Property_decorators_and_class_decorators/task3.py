class TypeDecorators:
    @staticmethod
    def to_type(func, final_type):
        def wrap_func(*args, **kwargs):
            return final_type(func(*args, **kwargs))

        return wrap_func

    @staticmethod
    def to_int(func):
        return TypeDecorators.to_type(func, int)

    @staticmethod
    def to_str(func):
        return TypeDecorators.to_type(func, str)

    @staticmethod
    def to_bool(func):
        return TypeDecorators.to_type(func, bool)

    @staticmethod
    def to_float(func):
        return TypeDecorators.to_type(func, float)


@TypeDecorators.to_int
def do_nothing(string):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing("25") == 25
assert do_something("True") is True
assert do_something("False") is True
assert do_something("") is False