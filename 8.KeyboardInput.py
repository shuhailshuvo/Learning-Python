# difference between input & raw_input is raw_input (in python 2) identify the data type automatically, which have been removed in python 3.
# However this feature can be achive by passing the input through eval() function.
# EVAL() EXECUTE THE GIVEN STRING AS PYTHON CODE. SO BE CAREFUL!!!

from getpass import getpass

# Printing title bar
print("\t**********************************************")
print("\t***     Understanding Keyboard input!      ***")
print("\t**********************************************\n")

# take string from user
print("Taking String input")
name = input("Your Name? ")
print("You typed: "+name+" of type:", type(name))

# take Number from user
print("Taking Number input")
age = input("Your Age? ")
print("You typed: "+str(age)+" of type:", type(age))

# take raw input from user
print("Taking Raw Input")
raw = input(" type anything")
print("You typed: "+raw+" of type:", type(raw))

# Parsing input
print("parsing input")
name, age, phone = input(
    "Enter your name, Age, Phone separated by space: ").split()
print("User Details: ", name, age, phone)


# Multiline input
print("Taking multiline input")
MultiLine = []
while True:
    line = input()
    if line:
        MultiLine.append(line)
    else:
        break
finalText = '\n'.join(MultiLine)
print("Final text input")
print(finalText)

# Auto type casting
print("Python 2 auto type casting input with eval")
anything = eval(input("Enter anything: "))
print(anything, type(anything))

# take password from user
print("Taking password input")
password = getpass("Enter your Password: ")
print("You typed: "+str(password)+" of type:", type(password))
