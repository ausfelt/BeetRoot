#Program that makes a random number between 1 and 10 and then you guess. If you are correct it will display a message and also when you are wrong
#Also, it will put the number that was randomly selected so you see that the program doesn't cheat on you ;)

from random import randint

random_number = str(randint(1, 10))
guess_number = input("Guess a number between 1 and 10, NO DECIMALS: ")

if random_number == guess_number:
    print(f"Congratulations! The number was indeed {random_number} :D")
else:
    print(f"Wrong! :( The number was {random_number}.")
