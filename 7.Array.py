from array import array

# array can contain only numeric item
# array can have elements of only one type
# passing float to create int array will result error, but passing int to create float array will automatically convert int to float and then added to array

# creating array
print("Creating integer array")
arr = array('i', [1, 2, 3, 4])
print(arr)

print("Creating float array")
arr2 = array('d', arr)
print(arr2)

# accessing array elements
print("accessing array elements")
print(arr[1], arr2[1])

# rest of operations like
#   - append
#   - extend
#   - remove
#   - pop
# are same as list
