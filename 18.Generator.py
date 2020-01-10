# If a function contains at least one yield statement, it becomes a generator function. Both yield and return will return some value from a function.
# The difference is that, while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later
# continues from there on successive calls.

# A simple generator function


def odds():
    n = 1
    yield n

    n += 2
    yield n

    n += 2
    yield n


print("iterating through generator")
oddNumber = odds()
print(next(oddNumber))
print(next(oddNumber))
print(next(oddNumber))

print("# using generator in loop")
for item in odds():
    print(item)

print("# Create generator using loop")

# infinite Generator


def evens():
    n = 0
    while n > -1:
        n = n+2
        yield n


evenNumber = evens()
print(next(evenNumber))
print(next(evenNumber))
print(next(evenNumber))
