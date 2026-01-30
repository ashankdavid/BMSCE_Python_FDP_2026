# Definition: A set is unordered collection of unique elements

# Properties
# Unordered # Order of hashing is considered
# Mutable
# Does not allow duplicates

mySet = {1,2,3,4,4}
print(mySet)

# Adding Elements
mySet.add(5)
print(mySet)

# Remove ELements
mySet.remove(2) # Remove will give a error if the element is not present
print(mySet)
mySet.discard(2) # Discard() will not give any error message
print(mySet)
mySet.pop()
print(mySet)
mySet.pop()
print(mySet)

setA = {1,2,3}
setB = {3,4,5}

union = setA | setB
print(union) #{1,2,3,4,5}
intersection = setA & setB
print(intersection) # {3}
diffrence = setA - setB
print(diffrence) # {1,2}