class Animal:
    def eat(self):
        print("Eating...")


class Dog(Animal):
    def bark(self):
        print("Barking...")

class Cat(Animal):
    def meow(self):
        print("Meowing...")


a = Animal()
d = Dog()
c = Cat()

a.eat()

d.eat()
d.bark()

c.eat()
c.meow()

