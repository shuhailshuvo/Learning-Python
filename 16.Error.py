
import sys


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


randomList = ['a', 0,  [1, 2], True]

for entry in randomList:
    # Comon exceptions
    r = None
    try:

        print("The entry is", entry)
        r = 1/int(entry)
        break
    except ValueError:
        print("Oops!", sys.exc_info()[0], "occured.,")
        print("ValueErrors are handled exclussively ")
        print()
        raise MemoryError("This is an argument")
        raise ValueTooSmallError("This is an argument")
    except:
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next entry.")
        print()

print("The reciprocal of", entry, "is", r)
