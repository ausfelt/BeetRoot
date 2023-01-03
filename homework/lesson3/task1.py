'''String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string
length is less than 2, return instead of the empty string.

Sample String: 'helloworld'

Expected Result : 'held'

Sample String: 'my'

Expected Result : 'mymy'

Sample String: 'x'

Expected Result: Empty String'''


modified_word = input("Give me a word please: ")

new_modified_word = modified_word[0:2] + modified_word[-2:]
if len(modified_word) <2:
   print("Sample Size to Small")

elif len(modified_word)>2:
    print(new_modified_word)

else:
    print(modified_word * 2)
