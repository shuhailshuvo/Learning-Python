# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
# Trying to access an element with non-existing index will raise an IndexError.
# The index must be an integer.otherwise, this will result into TypeError.
# append() method only works for addition of elements at the end of the List, for addition of element at the desired position, insert() method is used.
# extend() is used to add multiple elements at the end of the list.
# Python allows negative indexing for its sequences. The index of -1 refers to the last item

# Printing title bar
print("\t**********************************************")
print("\t***     Understanding List operations!     ***")
print("\t**********************************************\n")

# Creating
print("# Creating empty List", "==>", "empty_list=[]")
empty_list = []
print("list", empty_list, "Type:", type(empty_list))

print("# Creating List of String", "==>", "string_list=['a','c']")
string_list = ['a', 'c']
print("list", string_list, "Type:", type(string_list))

print("# Creating List of Numbers", "==>", "number_list=[-1,0,1,1e,3.1416]")
number_list = [-1, 0, 1, 3.1416, 1e5]
print("list", number_list, "Type:", type(number_list))

print("# Creating List of mixed data types",
      "==>", "mixed_list=[1,'s','','gr',8,True]")
mixed_list = ['', 1, 's', '', 'gr', 8, True]
print("list", mixed_list, "Type:", type(mixed_list))

print("# Creating List of list",
      "==>", "nested_list=[empty_list,string_list,number_list,mixed_list]")
nested_list = [empty_list, string_list, number_list, mixed_list]
print("list", nested_list, "Type:", type(nested_list))

print("# Creating list from loop", "==>",
      "pow2 = [2 ** x for x in range(10)]")
pow2 = [2 ** x for x in range(10)]
print("Power of 2:", pow2)


# Accessing
print("# Accessing element by index", "==>", "string_list[0]")
print("First Position:", string_list[0], ", Type:", type(string_list[0]))

print("# Accessing element by nested index", "==>", "nested_list[1][0]")
print("First Position:", nested_list[1][0], ", Type:", type(nested_list[1][0]))

print("# Accessing element by negative index", "==>", "string_list[-2]")
print("Second Last Position:",
      string_list[-2], ", Type:", type(string_list[-2]))

print("# Slicing list [start:end]", "==>", "string_list[0:2]")
print("Sliced:",
      string_list[0:2], ", Type:", type(string_list[0:2]))

print("# Get index of value", "==>", "string_list.index('a')")
print("index of 'a':", string_list.index('a'))

print("# Count element occurance", "==>", "string_list.count('a')")
print("number of 'a' in List:", string_list.count('a'))

print("# Sort list desc", "==>", "string_list.sort(reverse=True)")
string_list.sort(reverse=True)
print("Sorted:", string_list)

print("# Sort list asc", "==>", "string_list.sort()")
string_list.sort()
print("Sorted:", string_list)

print("# Sort list desc using sorted", "==>",
      "sorted(string_list,reverse=True)")
string_list = sorted(string_list, reverse=True)
print("Sorted:", string_list)

print("# Sort list asc using sorted", "==>",
      "sorted(string_list)")
string_list = sorted(string_list)
print("Sorted:", string_list)

print("# Copy List", "==>",
      "string_list.copy()")
new_string_list = string_list.copy()
print("Copied List:", new_string_list)

print("# Reverse List", "==>",
      "string_list.reverse()")
new_string_list.reverse()
print("Reversed List:", new_string_list)

print("# Check element", "==>",
      "'a' in string_list")
print("a is element of list:", 'a' in string_list)

# Add element to list
print("# Add single element", "==>", "string_list.append('new')")
string_list.append('new')
print("Updated List:", string_list)

print("# Add Multiple element", "==>", "string_list.extend(['e','f'])")
string_list.extend(['e', 'f'])
print("Updated List:", string_list)


# Update list element
print("# update single element", "==>", "string_list[2]='d'")
string_list[2] = 'd'
print("Updated List:", string_list)

print("# update single element using insert()",
      "==>", "string_list.insert(1,'b')")
string_list.insert(1, 'b')
print("Updated List:", string_list)

print("# update Multiple element", "==>",
      "string_list[0:6]=['P', 'Y', 'T', 'H', 'O', 'N']")
string_list[0:6] = ['P', 'Y', 'T', 'H', 'O', 'N']
print("Updated List:", string_list)

# Joining List
print("# Joining String & Mixed List", "==>", "string_list+mixed_list")
new_list = string_list+mixed_list
print("Updated List:", new_list)

# Repeating List
print("# Repeating String List", "==>", "string_list*50")
new_list = string_list*50
print("Updated List:\n", new_list)

# Removing element
print("# Removing Element by index using del", "==>", "del number_list[2]")
del number_list[2]
print("Updated List:\n", number_list)

print("# Removing Element by index using pop", "==>", "number_list.pop(0)")
number_list.pop(0)
print("Updated List:\n", number_list)

print("# Removing Element by Value using remove()",
      "==>", "number_list.remove(3.1416)")
number_list.remove(3.1416)
print("Updated List:\n", number_list)

print("# Removing All Elements", "==>", "number_list.clear()")
number_list.clear()
print("Updated List:\n", number_list)

print("# Removing Entire List", "==>", "del number_list")
del number_list
if "number_list" in locals():
    print("Updated List:\n", number_list)
else:
    print("List deleted ")

print("# Enumerate List", "==>", "print(enumerate(words))")
print(enumerate(string_list))

# List comprehension
print("List Comprehension on string")
letters = [letter for letter in "Python"]
print(letters)

print("List Comprehension on list")
elements = [element for element in string_list]
print(elements)

print("List Comprehension on list to modify element")
elements = ['<'+element+'>' for element in string_list]
print(elements)
