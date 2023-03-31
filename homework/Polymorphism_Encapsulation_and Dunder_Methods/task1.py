class Animal:
    def talk(self):
        print("I wish i knew what sound a class made")


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meoww")


def generic_talk(instance):
    instance.talk()


simon = Cat()
winston = Dog()

winston.talk()
generic_talk(winston)

simon.talk()
generic_talk(simon)