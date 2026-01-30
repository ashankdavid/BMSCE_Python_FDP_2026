# Definition: is mutable , unordered, collection of keyvalue pairs

# Properties

# Unordered (Python 3.7+ maintains the order of insertion)
# Mutable
# Keys should be unique

# Basic Operations

dict1 = {'name': 'Ashank', 'age': 35, 'city':'Bangalore'}
dict2 = {'name': 'David', 'age': 40, 'city':'Bangalore'}
dict3 = {'name': ['Ashank', 'David'],
         'ages':[35, 40],
         'cities':['bangalore', 'bangalore']}

# Printing Dictionaries and accessing the values
print(dict1)
print(dict1['name'])

# Adding some values
dict1['job'] = 'Trainer'
print(dict1)
dict2['job'] = 'Trainer'
print(dict2)

# Removing the elements from dictionaries
# 1) pop()
# 2) popitem()
# 3) del
# 4) clear()

# 1) pop()
dict1.pop('age')
print(dict1)

# 2) popitem() it will delete the latest key from the dictionary
dict1.popitem()
print(dict1)

# del key
del dict2['age']
print(dict2)

# 4) clear()
dict3.clear()
print(dict3)

# Dictionaries Functions

# 1) keys()
# 2) values()
# 3) items()
# 4) get(key)
# 5) update()

myDict = {'name' : 'Ashank',
          'age' : 35,
          'city' : 'Bangalore'}

# 1) Key()
key = myDict.keys()
print(key) # directly printing keys
print(type(key)) # trying to check the key type
for i in key:
    print(i) # iterate overs keys and printing them seperatly
print(list(key)) # keys as list

# 2) Values
value = myDict.values()
print(value)
print(type(value))
for i in value:
    print(i)
print(list(value))

# 3) items()
item = myDict.items()
print(item)
print(type(item))
for i in item:
    print(i)
print(list(item))

# get()
print(myDict.get('name'))
print(myDict.get('city'))
print(myDict.get('age'))

# update()
myDict.update({'city': 'Pune'})
print(myDict)
