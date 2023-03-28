

def total_price(dictionary_1, dictionary_2):
    total_price = 0
    for key in dictionary_1:
        total_price += dictionary_1[key] * dictionary_2[key]
    return total_price

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


print(total_price(stock, prices))
