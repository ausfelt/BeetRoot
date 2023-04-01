def stop_words(words: list):
    def decorator_function(func):
        def wrapper(name):
            sequence = func(name)
            for word in words:
                if word in sequence:
                    sequence = sequence.replace(word, '*')
            return sequence

        return wrapper

    return decorator_function


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

# Just to see that it works
print(create_slogan("Steve") == "Steve drinks * in his brand new *!")

