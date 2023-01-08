#Exclusive common numbers.
#Generate 2 lists with the length of 10 with random integers from 1 to 10, and
#make a third list containing the common integers between the 2 initial lists without any duplicates.
#Constraints: use only while loop and random module to generate numbers

#Find the common numbers. Between 1-20 in this case.

from random import sample

list_1 = sample(range(1, 20), 11)
list_2 = sample(range(1, 20), 11)
print(f"list 1:\n{list_1}\n\nlist2:\n{list_2}\n")

x = 0
my_set = set()

while x < len(list_1):
    if list_1[x] in list_2:
        my_set.add(list_1[x])
    x += 1

print(f"The final common numbers are:\n{my_set}")
