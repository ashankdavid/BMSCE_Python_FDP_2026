def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    operation = int(input("Enter a Operation\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Exit\n"))

    if 0<operation<5:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
    else:
        break

    match operation:
        case 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
        case 2:
            print(f"{num1} - {num2} = {sub(num1, num2)}")
        case 3:
            print(f"{num1} * {num2} = {mul(num1, num2)}")
        case 4:
            print(f"{num1} / {num2} = {div(num1, num2)}")
        case 5:
            print("OKAY BYEEE")
            break
        case _:
            print("Invalid Choice!")
