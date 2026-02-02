class Student:
    def __init__(self, name, usn):
        self.name = name
        self.usn = usn

    def printDetails(self):
        print(f"Student name is {self.name}")
        print(f"Student USN is {self.usn}")

name1 = input("Enter a Name1: ")
usn1 = int(input("Enter a USN1: "))

name2 = input("Enter a Name2: ")
usn2 = int(input("Enter a USN2: "))

s1 = Student(name1, usn1)
s2 = Student(name2, usn2)

s1.printDetails()
s2.printDetails()