# a decorator takes in a function, adds some functionality and returns it.
from colorama import init, Fore, Style
init()


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def dot(func):
    def inner(*args, **kwargs):
        print("." * 30)
        func(*args, **kwargs)
        print("." * 30)
    return inner


def dash(func):
    def inner(*args, **kwargs):
        print("-" * 30)
        func(*args, **kwargs)
        print("-" * 30)
    return inner


def red(func):
    def inner(*args, **kwargs):
        print(Fore.RED)
        func(*args, **kwargs)
        print(Style.RESET_ALL)
    return inner


def blue(func):
    def inner(*args, **kwargs):
        print(Fore.BLUE)
        func(*args, **kwargs)
        print(Style.RESET_ALL)
    return inner


def green(func):
    def inner(*args, **kwargs):
        print(Fore.GREEN)
        func(*args, **kwargs)
        print(Style.RESET_ALL)
    return inner


@dash
@dot
@star
@green
@dot
@blue
@dash
@red
def printer(msg):
    print(msg)


printer("Hello")
