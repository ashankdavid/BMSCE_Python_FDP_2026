# Definition: A Tuple is ordered, immutable collection of items
from itertools import count

# Properties
# Ordered
# Immutable
# Allows Duplicates

myTuple = (1, 2.5, "BMSCE", "A", 4, 2.5)
anotherTuple = tuple(range(10))

# Access the elements from tuple
print(myTuple)
print(myTuple[0])
print(myTuple[2])
print(myTuple[1:3])
print(myTuple[-1])
print(myTuple[-2])

# Operations on Tuples

# 1) Concatenation of 2 tuples using + Operator

tuple1 = (1,2,3)
tuple2 = (4,5,6)

resultTuple = tuple1 + tuple2
print(resultTuple)

# 2) Repitation of tuples
originalTuple = (1,2,3)
repeatedTuple = originalTuple * 3
print(repeatedTuple)

# 3) Membership of an element insiode the tuple
sampleTuple = (1,2,3,4,5,6)
print(3 in sampleTuple)
print(20 in sampleTuple)
print(3 not in sampleTuple)
print(20 not in sampleTuple)

# Length of a tuple
Length = len((4,5,73,1,7,3,6,0))
print(Length)

# Index() find out the index of an elemtn in a tuple
index = myTuple.index("BMSCE")
print(index)

# Count() counting the number of occurances of an element inside the tuple
count = myTuple.count(2.5)
print(count)

# Note - THere are only 2 inbuilt functions in tuple - index and count
# Why? - because tuples are immutable, they cannot be modified
# sooo we have very limited options in tuple

# Once the Tuple is created you cannot change anything in it
# This is TUPLE