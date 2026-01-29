name = input("Enter your name: ")
BirthYear = int(input("Enter your BirthYear: "))
print(type(BirthYear))
currentYear = int(input("Enter the current year: "))
print(type(currentYear))
age = currentYear - BirthYear

# Original Printing way
print(name + " Your age is " + str(age))
print("your name: ", name, "your age: ", age)

# Formatted Strings way
print(f"{name} your age is {age}") # Easiest Way
print("{}Your age is {}".format(name, age))