
from colorama import init, Fore, Style
init()


def draw(bits):
    for bit in bits:
        if bit == "0":
            print(Fore.GREEN + ".", end='')
        else:
            print(Fore.RED + ".", end='')
    print(Style.RESET_ALL)


def warn(msg):
    print(Fore.RED + msg)
    print(Style.RESET_ALL)


def error(msg):
    print(Fore.RED + msg)
    print(Style.RESET_ALL)


def isBinary(numberString):
    uniqueSet = set(numberString)
    return uniqueSet.issubset({"0", "1"})


def formatNumber(numberString, title):
    if isBinary(numberString):
        return numberString
    else:
        warn('Opps! I don\'t understand decimal. Binary is the only option.')
        return prompt(title)


def prompt(title):
    userInput = input(title + ": \t")
    if userInput.isnumeric():
        return formatNumber(userInput, title)
    else:
        error('Only Numbers are accepted')
        return prompt(title)


first_number = prompt("Enter a number")
second_number = prompt("Enter another number")
draw(first_number)
draw(second_number)
print("This is exatly how computer displays")
