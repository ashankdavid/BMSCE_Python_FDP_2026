fruit = input("Enter a Fruit: ")

match fruit:
    case "Apple":
        print("You have given an Apple")
    case "Mango":
        print("You have given a Mango")
    case _:
        print("Invaild String Entered")