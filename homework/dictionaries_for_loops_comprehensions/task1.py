

sentence = input("Type a sentence without punctuation here, please: ")
keys = sentence.lower().split()

our_dictionary = {}

for words in keys:
    if words in our_dictionary:
        our_dictionary[words] += 1
    else:
        our_dictionary[words] = 1

print(our_dictionary)
