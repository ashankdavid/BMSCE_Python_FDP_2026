from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    def run(self):
        print("Running...")

class Dog(Animal):
    def eat(self):
        print("Dog Food")

    def bark(self):
        print("Barking...")

# a = Animal() # this will give you an error
d = Dog()

# a.eat()

d.eat()
d.bark()
d.run()