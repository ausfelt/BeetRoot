def mult(a: int, n: int) -> int:
    if a == 0 or n == 0:
        return 0

    if n < 0:
        return -a + mult(a, n+1)
    else:
        return a + mult(a, n-1)


assert mult(2, 4) == 8
assert mult(-2, 4) == -8
assert mult(2, 0) == 0
assert mult(2, -4) == -8
assert mult(-2, -4) == 8


#Testing
print(mult(-5, 6))