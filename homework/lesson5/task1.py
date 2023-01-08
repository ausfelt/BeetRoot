#The greatest number

#Write a Python program to get the largest number
#from a list of random numbers with the length of 10
#Constraints: use only while loop and random module to generate numbers

#How many numbers to pick, how high it can get an how many in the list

from random import sample

random_number = sample(range(1, 3000), 10)
x = 0
biggest_number = 0

while x < len(random_number):
    if random_number[x] > biggest_number:
        biggest_number = random_number[x]
    x += 1

print(random_number)
print(biggest_number)
