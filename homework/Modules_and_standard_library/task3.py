import os

def count_lines(name):
    with open(name, 'r') as f:
        lines = f.readlines()
    return len(lines)

def count_chars(name):
    with open(name, 'r') as f:
        chars = f.read()
    return len(chars)

# define the input file name
filename = 'my_file.txt'

# call the count_lines() and count_chars() functions with the input file name
lines = count_lines(filename)
chars = count_chars(filename)

# print the line and character counts
print(f"Lines: {lines}")
print(f"Characters: {chars}")