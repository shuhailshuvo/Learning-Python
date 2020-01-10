# Dictionary keys are case sensitive, same name but different cases of Key will be treated distinctly.
# Dictionary elements can't be accessed by position like list
# Dict.setDefault(key, value) Method look for the value. if not present, set the default one
# del Dict will delete the entire dictionary and hence printing it after deletion will raise an Error.

# Creating Dict
print("Creating an empty Dictionary")
dict1 = {}
print(dict1)

print("Creating a Dictionary with Integer Keys")
dict2 = {1: 'A', 2: 'B', 3: 'C'}
print(dict2)

print("Creating a Dictionary with Mixed keys")
dict3 = {'Name': 'A', 1: dict2}
print(dict3)

print("Creating a Dictionary with dict() method")
dict4 = dict({1: 'A', 2: 'B', 3: 'C'})
print(dict4)

print("Creating a Dictionary with each item as a Pair")
dict5 = dict([(1, 'A'), (2, 'B')])
print(dict5)

print("Creating a Dictionary with given sequence")
dict7 = dict.fromkeys({'a', 'b', 'c', 'd', 'e'}, True)
print(dict7)

# accessing Dictionary elements
print("Acessing an element using key:")
print(dict2[1], dict3[1], dict3[1][3])

print("Acessing an element using get():")
print(dict3[1].get(1))

print("Acessing only values:")
print(dict2.values())

print("Acessing only keys:")
print(dict2.keys())

print("Acessing key:value tupple:")
print(dict2.items())

print("String representation of Dictionary")
print(str(dict2))

# copy Dictionary
print("Copying dict2:")
dict6 = dict2.copy()
print(dict6)

# using setdefault() method
print("using setdefault() method:", dict1)
dict1.setdefault('b', 1)
print("Dictionary:", dict1)

# Adding element to a Dictionary
print("Adding Element")
dict1['a'] = 1
print(dict1)

print("adding a Nested Key: ")
dict4 = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print(dict4)

# Updating element value
print("Updated value: ")
dict1[1] = 'Welcome'
print(dict4)

print("Updated value using update(): ")
dict1.update({"a": 1})
print(dict1)

# Deleting a Key value
print("Deleting a specific key: ")
del dict4['Nested']
print(dict4)

print("Deleting a Key using pop()")
dict2.pop(1)
print(dict2)

print("Pops an arbitrary key-value pair: ")
dict5.popitem()
print(dict5)

print("Deleting Entire Dictionary: ")
dict3.clear()
print(dict3)
