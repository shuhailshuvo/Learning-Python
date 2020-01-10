# Decimal.as_tuple() returns the decimal number as tupple with sign, digits & exponent
# To find length of a number type, you need to convert it to string first
# Python can define infinity!!! try this:
#       print(float('Inf'), type(float('Inf')), float('Inf') > 999999999999999999999999999999999999999999)

from decimal import Decimal
from fractions import Fraction


number1 = 1
number2 = 1.0
number3 = 1+2j

# types
print("Number types")
print(type(number1), type(number2), type(number3))

# Conversion
print("convert float (1.0) to int")
print(int(number2))

print("convert int (1) to float")
print(float(number1))

print("convert int (1) to complex")
print(complex(number1))

print("convert float (1.0) to complex")
print(complex(number2))

# Fractions
print("Get the fraction of int 5")
print(Fraction(5))

print("Get the fraction of float 1.1")
print(Fraction(1.1), "\n This is not preffered way to do that.")

print("Get the fraction of string 1.1")
print(Fraction('1.1'))

print("Converting float to hex")
print(float.hex(1.1))

result = input("Can you sum 1.1 + 2.2 ?")
if result == (1.1+2.2):
    print("Great!")
else:
    print("Wrong!!!\nThis is: ", (1.1+2.2))
    print("decimal value of 1.1: ", Decimal(1.1))
    print("decimal value of 2.2: ", Decimal(2.2))

result = input("What you think 0.1 + 0.1 + 0.1 - 0.3 ?")
if result == (0.1 + 0.1 + 0.1 - 0.3):
    print("Great!")
else:
    print("Wrong!!!\nThis is: ", (0.1 + 0.1 + 0.1 - 0.3))
    print("decimal value of 0.1: ", Decimal(0.1))
    print("decimal value of 0.1 + 0.1 +0.1: ",
          Decimal(0.1) + Decimal(0.1) + Decimal(0.1))
    print("decimal value of 0.3: ", Decimal(0.3))

print("""
\t\t Floating-point numbers are represented in computer hardware as base 2 (binary) fractions.
\t\t Unfortunately, most decimal fractions cannot be represented exactly as binary fractions. 
\t\t A consequence is that, in general, the decimal floating-point numbers you enter are only 
\t\t approximated by the binary floating-point numbers actually stored in the machine.
\t\t Using Python's decimal class would give you better results.\n\n
\t\t\t\t\t WELCOME TO PYTHON
""")
