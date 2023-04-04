def sum_of_digits(digit_string: str) -> int:
    if not digit_string.isdigit():
        raise ValueError("input string must be a number")
    else:
        digit_string = int(digit_string)

    if digit_string == 0:
        return 0
    else:
        return digit_string % 10 + sum_of_digits(str(digit_string // 10))


# assert sum_of_digits('test') == ValueError("input string must be digit string")
assert sum_of_digits('26') == 8
assert sum_of_digits('1234') == 10

#Testing testing
print(sum_of_digits("55"))
print(sum_of_digits("54998"))
print(sum_of_digits("abcde")) #Should raise ValueError


