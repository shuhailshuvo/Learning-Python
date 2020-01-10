# Lambda is anonymous function
# Difference between map, filter & reduce is map apply mapping function to each element and return, reduce apply the supplied function on all item and return combined result, filter apply the filtering rules and return subset of given list.
from time import sleep
import functools
# function


def simpleFunction():
    '''This is a docstring. I have created a new function'''
    print("call from Simple function")


# with arguments
def simpleFunctionWithArgs(args1, args2):
    print("call from Simple function", args1, args2)


def simpleFunctionWithArgsExtract(*args):
    args1, args2 = args
    print("call from Simple function", args1, args2)


def simpleFunctionWithArgsKey(**args):
    args1, args2 = args
    print("call from Simple function", args1, args2)
# return


def simpleFunctionWithReturn():
    return "Return from simpleFunctionWithReturn()"


def simpleFunctionWithMultiReturn():
    return "Return", "from", "simpleFunctionWithMultiReturn()"

# lambda


def sum(x, y): return x+y


# Docstring
print(simpleFunction.__doc__)


simpleFunction()
simpleFunctionWithArgs(1, 2)
simpleFunctionWithArgsExtract(1, 2)
simpleFunctionWithArgsKey(a=1, b=2)
print(simpleFunctionWithReturn())
print(simpleFunctionWithMultiReturn())

# built-in functions
print("\n\nBuilt-in Functions\n\nAbsolute value of a number:\n\t",
      "abs(-1) == abs(1)", abs(-1) == abs(1))

list = [1, True, "TRUE", "true", "True"]
dict = {"a": True, "b": 1}
print('All()', '\n\tall([1, True, "TRUE", "true", "True"])', all(list),
      '\n\tall({"a": True, "b": 1})', all(dict))

list = [1, False, "a", "b", "0"]
dict = {"a": True, "b": 0}
print('Any()', '\n\tany([1, True, "TRUE", "true", "True"])', any(list),
      '\n\tany({"a": True, "b": 1})', any(dict))

print("ASCII()\n\t", 'ascii("/bɛŋˈɡɔːli/") => ', ascii("/bɛŋˈɡɔːli/"))

print("bin()\n\t", 'bin(255) => ', bin(255))

print("bool()\n\t", 'bool("true") => ', bool("true"))

print("chr()\n\t", 'chr(126) => ', chr(126))
itr = iter({"a": True, "b": 1})
print("iter()\n\t", 'iter({"a": True, "b": 1}) => ', itr)

print("len()\n\t", 'len({"a": True, "b": 1}) => ', len({"a": True, "b": 1}))

print("max()\n\t", 'max([2,50,35,15,22,67,59,0]) => ',
      max([2, 50, 35, 15, 22, 67, 59, 0]))

print("min()\n\t", 'min([2,50,35,15,22,67,59,0]) => ',
      min([2, 50, 35, 15, 22, 67, 59, 0]))

print("next()\n\t", 'next(iter({"a": True, "b": 1})) => ',
      next(itr))

print("repr()\n\t", 'repr({"a": True, "b": 1}) => ', repr({"a": True, "b": 1}))


def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print("map()\n\t", 'map(addition, numbers) => ', result)

# Or, using lambda
result = map(lambda x: x + x, numbers)
print(result)

print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, result))

newList = filter(lambda x: x > 4, numbers)
print(newList)
