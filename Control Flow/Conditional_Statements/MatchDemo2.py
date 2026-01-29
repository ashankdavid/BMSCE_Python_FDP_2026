month = int(input("Enter a Month Num "))

match month:
    case 1:
        print("Jan")
    case 2:
        print("Feb")
    case 3:
        print("Mar")
    case _:
        print("Invaild Month")
