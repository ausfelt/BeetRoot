'''The name check.

Write a program that has a variable with your name stored (in lowercase) and then 
asks for your name as input. The program should check if your input is equal to the 
stored name even if the given name has another case, e.g., if your input is “Anton” 
and the stored name is “anton”, it should return True.'''

my_name = "linus"
correct_or_false_name = True

while correct_or_false_name:
    my_name_input = input("Say my name: ") #Breaking Bad reference. Sorry, i had to do it.
    if my_name_input.lower() == my_name:
        print("Yes that is indeed my name. GG")
        correct_or_false_name = False
    else:
        print("Come on, it's only 5 letters and we have know each other 14 years :( ")
