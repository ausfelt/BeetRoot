class Dog:

    age_factor = 7

    def __init__(self, name, dog_age):
        self.name = name
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * Dog.age_factor


the_dog = Dog("Bingo", 5)
print(f"In human years, {the_dog.name} is: {the_dog.human_age()} years old.")