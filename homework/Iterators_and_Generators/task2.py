def in_range(start, end, step=1):
    while start < end:
        yield start
        start += step


for e in in_range(2, 25, 4):
    print(e)