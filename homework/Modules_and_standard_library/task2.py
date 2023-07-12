import sys

# Default path
print(sys.path)

# Append new path to the existing one
sys.path.append('/homework/Modules_and_standard_library/module1.py')
print(sys.path)

# Define the entire path
sys.path = '/homework/Modules_and_standard_library/module1.py'
print(sys.path)

try:
    import numpy
except SystemError:
    print('Works!')

# I don't know why but the numpy is messing with the program but i know it should work
