# set() method should be used to create empty set
# set will contain unique items
# Difference between Discard() & Remove() is, remove raise error
# Frozensets are sets with out the support of add or remove


# creating set
print("creting empty set")
set1 = set()
print(set1)

print("creting set with element")
set2 = {1, 2, 3, 4}
print(set2)

print("creting set from list")
set3 = set([1, 3, 5, 7])
print(set3)

# adding set element
print("Add element to set")
set2.add(6)
print(set2)

# updating set element
print("update set")
set2.update({2, 4, 6, 8})  # must be list or tupple
print(set2)

# Removing set element
print("Remove element from set")
set2.remove(1)
print(set2)

print("Remove element from set using discard")
set2.discard(3)
print(set2)

# Union
print("union on sets2 using |")
print(set2 | set3)

print("union on sets using union()")
print(set2.union(set3))

# intersact
print("intersact on sets2 using &")
print(set2 & set3)

print("intersact on sets using intersection()")
print(set2.intersection(set3))

# intersact
print("intersact on sets2 using &")
print(set2 & set3)

print("intersact on sets using intersection()")
print(set2.intersection(set3))

# Difference
print("Difference between sets")
print(set2, set3, set2 - set3)

# Symmetric difference
print("Symmetric Difference between sets")
print(set2 ^ set3)
