def function_1():
    print("Here i am :D")


def function_2():
    return function_1


access_function_1 = function_2()
access_function_1()

