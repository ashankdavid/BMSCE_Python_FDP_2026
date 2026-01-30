# Definition - A list is ordered, mutable collection of items

# Properties
# Ordered
# Mutable
# Allows Duplicates

myList = [1,2,3,4,5]  # Syntax using []
anotherList = list(range(2, 101, 2))

# Operations on List
# 1) Access Elements from myList
print(myList)
print(f"on 3rd index we have {myList[3]}")
print(f"on 0th index we have {myList[0]}")
print(myList[2:4]) # [3,4]
print(f"Another list is {anotherList}")
print(anotherList[10:25])
print(f"On the last index we have {anotherList[-1]}")
# in the above example -ive index starts from last element in the list

# 2) Modifying the Elements
# Because Lists are mutable we can Modify Lists
myList[3] = 400
print(myList)

# 3) Printing the list
# 2 ways of printing the list or any collection in python
# 1st way
print(myList)
# 2nd way
for i in myList:
    print(i, end=" ")
print()

# 4) Adding an elements to a list
# append() it will ad the element at the last of the list
myList.append(6)
myList.append(7)
print(myList)
for i in range(8, 11):
    myList.append(i)
print(myList)

# insert() it will inser the element at a particular position in the list
myList.insert(6, 5000)
print(myList)
myList.insert(3, "BMSCE")
print(myList)

# 5) Removing the elements from List
myList.remove(5000)
print(myList)
myList.pop() # remove the last index
print(myList)
del myList[3]
print(myList)

# 6) other functions
print(f"Length of myList is {len(myList)}")
myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)
