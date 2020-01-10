
def takeNumber(prompt):
    userInput = input(prompt)
    if(userInput.isdigit()):
        return int(userInput)
    else:
        print("Only numbers are allowed")


print("While Loop")
i = 10
while(i > 0):
    print("in ", i, " seconds")
    i -= 1

print("For Loop")
i = 10
for j in range(20, 10, -1):
    print("in ", i-j, " seconds")


print("Recursion")


def rec(i):
    if(i > 0):
        print("in ", i, " seconds")
        rec(i-1)


rec(10)

#
# #
# # #
# # # #
# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
for number in range(1500, 2700, 5):
    if(number % 7 == 0):
        print(number)

#
# #
# # #
# # # #
# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]


def celsius2fahrenheit(temp):
    return (temp*(9/5))+32


def fahrenheit2celsius(temp):
    return (temp-32*(5/9))


userInput = eval(input("Convert to celsius\n"))
print(userInput, " Fahrenheit = ", fahrenheit2celsius(userInput), " Celsius")
userInput = eval(input("Convert to fahrenheit\n"))
print(userInput, " Celsius = ", celsius2fahrenheit(userInput), " Fahrenheit")

#
# #
# # #
# # # #
# Write a Python program to guess a number between 1 to 9.
number = int(1)
while True:
    guess = input("Guess a number between 1-9\n")
    if(guess.isdigit() == False):
        print("Please enter only number between 1-9")
        continue
    guess = int(guess)
    if(0 < guess < 10):
        if(number == guess):
            print("Good Guess :)")
            break
        else:
            print(":(")
            print(type(number), type(guess))
    else:
        print("Please enter number between 1-9")
#
# #
# # #
# # # #
# # # # #
# # # #
# # #
# #
#
# Write a Python program to construct the above pattern

max = takeNumber("Enter a number: \n")
for i in range(1, max):
    print(" # "*i+"\n")

for i in reversed(range(1, max-1)):
    print(" # "*i+"\n")

#
# #
# # #
# # # #
# Write a Python program that accepts a word from the user and reverse it.

name = input("Enter your name: \n")

for i in reversed(name):
    print(i, end="")

#
# #
# # #
# # # #
# Write a Python program to count the number of even and odd numbers from a series of numbers.

series = [-1, -3, 4, -2, 4, 2, 1, 4, 2, 9, -5]
even = 0
odd = 0

for number in series:
    if(number % 2 == 0):
        even += 1
    else:
        odd += 1
else:
    print("Total evens: ", even, " & odds: ", odd)

#
# #
# # #
# # # #
# Write a Python program that prints each item and its corresponding type from the following list.

datalist = [1452, 11.23, 1+2j, True, 'w3resource',
            (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for data in datalist:
    print(data, type(data))

#
# #
# # #
# # # #
# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(0, 6):
    if(i % 3 == 0):
        continue
    print(i, end=", ")
print("\n\n")
#
# #
# # #
# # # #
# Write a Python program to get the Fibonacci series between 0 to 50
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.

number = 1
last = 0
fab = [0]
while number <= 50:
    fabNum = number
    fab.append(fabNum)
    number = number + last
    last = fabNum
else:
    print(fab)

#
# #
# # #
# # # #
# Write a Python program that accepts a string and calculate the number of digits and letters.

digits = 0
letters = 0

for x in "Happy New Year 2020":
    if x.isalpha():
        letters += 1
    if x.isdigit():
        digits += 1
else:
    print("digit: ", digits, ", letters: ",
          letters, "in 'Happy New Year 2020'")

#
# #
# # #
# # # #
# Write a Python program to create the multiplication table (from 1 to 10) of a number

number = takeNumber("Enter a Number\n")
for multiplier in range(1, 11):
    print(type(number), type(multiplier))
    print(number, " X ", multiplier, " = ", number*multiplier)
