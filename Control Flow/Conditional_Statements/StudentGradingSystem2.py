m1 = int(input("Enter the Marks1: "))
m2 = int(input("Enter the Marks2: "))
m3 = int(input("Enter the Marks3: "))
m4 = int(input("Enter the Marks4: "))
m5 = int(input("Enter the Marks5: "))
total_Marks = 500
if 0 <= m1 <= 100:
    if 0 <= m2 <= 100:
        if 0 <= m3 <= 100:
            if 0 <= m4 <= 100:
                if 0 <= m5 <= 100:
                    percentage = ((m1+m2+m3+m4+m5)/total_Marks) * 100
                    if percentage >= 75:
                        print("A")
                    elif percentage >= 50:
                        print("B")
                    elif percentage >=30:
                        print("C")
                    else:
                        print("Fail")
                else:
                    print("Marks 5 are Invaild")
            else:
                print("Marks 4 are Invaild")
        else:
            print("Marks 3 are Invaild")
    else:
        print("Marks 2 are Invaild")
else:
    print("Marks 1 are Invaild")
