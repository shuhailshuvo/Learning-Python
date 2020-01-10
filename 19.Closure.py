# We must have a nested function (function inside a function).
# The nested function must refer to a value defined in the enclosing function.
# The enclosing function must return the nested function.


def calculate(num1, num2):
    def sum():
        return num1+num2

    def substract():
        return num1-num2

    return sum, substract


sum, substract = calculate(7, 6)
print(calculate(7, 6))
print(sum())
print(substract())

# When there are few methods to be implemented in a class, closures can provide an alternate and more elegant solutions.
