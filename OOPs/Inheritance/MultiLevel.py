class Animal:
    def eat(self):
        print("Eating...")


class Dog(Animal):
    def bark(self):
        print("Barking...")

class Puppy(Dog):
    def sleep(self):
        print("Sleeping...")


a = Animal()
d = Dog()
p = Puppy()

a.eat()

d.eat()
d.bark()

p.eat()
p.bark()
p.sleep()