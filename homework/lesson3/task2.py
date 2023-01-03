'''The valid phone number program.

Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and
is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.'''

# I tried to make a little more advanced number calculator but the else statement is always showing

#phone_number = input("Please put a valid phone number here: ")

#if phone_number.isnumeric() is True and len(phone_number) == 10:
#   print("This could be a valid number")

#elif phone_number.isnumeric() is True and len(phone_number) < 10:
#    print("This number is too short")

#else: phone_number.isnumeric() is True and len(phone_number) > 10
#print("You have entered to many digits")

# This is the easy one that works

phone_number = input("Please put a valid phone number here")

if phone_number.isnumeric() is True and len(phone_number) == 10:
    print("This is a valid number")
else:
    print("This is not a valid number")
