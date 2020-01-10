
# To write multiline expression use \ at the end of each line.
# Strings are immutables, unless assigned to new variable
# String can be formatted using f-string, {} or %
# ord() => integer representing the Unicode code point of the character

# import required packages
from datetime import datetime
import string

# variables
word = "hi"
number = 50
short_text = "hey there"
long_text = "a very long text"
chars = string.ascii_lowercase +\
    string.ascii_uppercase +\
    string.digits +\
    string.hexdigits +\
    string.octdigits +\
    string.whitespace +\
    string.punctuation
size = 64
date_str = '09-19-2018'
date_object = datetime.strptime(date_str, '%m-%d-%Y').date()

# Printing title bar (using tab)
print("\t**********************************************")
print("\t***    Understanding String operations!    ***")
print("\t**********************************************\n")

# printing
print("# printing string", "==>", "print('hi')")
print("hi")

print("# Spliting string into list", "==> '"+short_text+"'.split(' ')")
words = short_text.split(" ")
print(words)

print("# printing multiline", "==>", 'print("""...""")')
print("""
this is line 1
this is line 2
""")

print("# Repeating string", "==>", "print('"+words[0]+"'*3)")
print(words[0]*3)

print("# Strings are immutables, unless assigned to new variable",
      "==>", "word+'per'\nprint('word')")
word + "per"
print(word)
# https://stackoverflow.com/questions/9097994/arent-python-strings-immutable-then-why-does-a-b-work

print("# Joining list to string, joiner will be removed automatically from the end",
      "==>", "print('+'.join(list))")
print("+".join(words))

print("# printing string with number", "==>", 'print(number, "cent")')
print(number, "cent")

print("# converting number into string & concate with another",
      "==>", 'print("H"+str(3110)+" W"+str(0)+"R"+str(1) + "D")')
print("H"+str(3110)+" W"+str(0)+"R"+str(1) + "D")

print("# String Formatting with the % Operator",
      "==>", 'print("%s %s" % ("hello", "world"))')
print("%s %s" % ("hello", "world"))

print("# String Formatting with the {}", "==>",
      'print("{0} {1}".format("hello", "world"))')
print("{0} {1}".format("hello", "world"))

print("# String Formatting with the f-string", "==>",
      "print(f'{short_text}{' '}{long_text}')")
print(f'{short_text}{" "}{long_text}')

print("# String reverse using slice(start:stop:step)",
      "==>", "print(long_text[::-1])")
print(long_text[::-1])

print("# Trimming leading & trailing space", "==>", 'print(" a b ".strip())')
print(" a b ".strip())

print("# Make Upper Case", "==>", "print(short_text.upper())")
print(short_text.upper())

print("# Make Lower Case", "==>", "print(short_text.lower())")
print(short_text.lower())

print("# Capitalize string", "==>", "print(long_text.capitalize())")
print(long_text.capitalize())

upper = "ABC"
lower = "abc"
print("# String comparisn using case fold", "==>",
      "print("+upper+".casefold()=="+lower+".casefold())")
print(upper.casefold() == lower.casefold())

print("# swap case of a string (upper-lower)",
      "==>", 'print(short_text.swapcase())')
print(short_text.swapcase())
print(short_text.swapcase().swapcase())

print("# Replace string", "==>", 'print("'+short_text+'".replace("h","_"))')
print(short_text.replace("h", "_"))

print("# Replace only the 1st occurance", "==>",
      'print("'+short_text+'".replace("h","_",1))')
print(short_text.replace("h", "_", 1))

print("# define Tab size", "==>", 'print('+short_text +
      '.replace(" ","\t").expandtabs(tabsize=3))')
print(short_text.replace(" ", "\t").expandtabs(tabsize=3))

print("# string translation (multiple replace)", "==>",
      short_text+".maketrans({ord('h'): 'a', ord('e'): ord('r')})")

translation = short_text.maketrans(
    {ord('h'): 'b', ord('e'): ord('o')})
print(short_text.translate(translation))

print("# string Count number of occurence",
      "==>", "print("+long_text+".count('e'))")
print(long_text.count("e"))

print("# Find first occurance position of string",
      "==>", 'print('+long_text+'.find("e"))')
print(long_text.find("e"))

print("# Find last occurance position of string (reverse find)",
      "==>", 'print('+long_text+'.rfind("e"))')
print(long_text.rfind("e"))

print("# String index (first occurence) (returns error instead of -1 for unmatched)",
      "==>", 'print('+short_text+'.index("t"))')
print(short_text.index("t"))

print("# String reverse index (last occurence) (returns error instead of -1 for unmatched)",
      "==>", 'print('+short_text+'.index("t"))')
print(short_text.index("t"))

print("# partition string into 3 part. before, separator, after",
      "==>", 'print(short_text.partition("e"))')
print(short_text.partition("e"))

print("# reverse partition string into 3 part. before, separator, after",
      "==>", 'print(short_text.rpartition("e"))')
print(short_text.rpartition("e"))

print("# Split lines of a string", "==>", 'print(long_text.splitlines())')
print(long_text.splitlines())

print("# check if string starts with given keyword",
      "==>", 'print('+long_text+'.startswith("a"))')
print(long_text.startswith("a"))

print("# check if string ends with given keyword",
      "==>", 'print('+long_text+'.endswith("text"))')
print(long_text.endswith("text"))

print("# check if string contains given keyword",
      "==>", 'print('+short_text+'.__contains__("t"))')
print(short_text.__contains__("t"))

print("# Check if string is alphanumeric",
      "==>", 'print('+short_text+'.isalnum())')
print(short_text.isalnum())

print("# Check if string is Alpha", "==>", "print("+short_text+".isalpha())")
print(short_text.isalpha())

print("# Check if string is Decimal", "==>",
      "print("+short_text+".isdecimal())")
print(short_text.isdecimal())

print("# Check if string is Digit", "==>", "print("+short_text+".isdigit())")
print(short_text.isdigit())

print("# Check if string is valid Identifier",
      "==>", "print("+short_text+".isidentifier())")
print(short_text.isidentifier())

print("# Check if string is lower", "==>", "print("+short_text+".islower())")
print(short_text.islower())

print("# Check if string is upper", "==>", "print("+short_text+".isupper())")
print(short_text.isupper())

print("# Check if string is Numeric", "==>",
      "print("+short_text+".isnumeric())")
print(short_text.isnumeric())

print("# Check if string is Printable", "==>",
      "print("+short_text+".isprintable())")
print(short_text.isprintable())

print("# Check if string is Space", "==>", "print("+short_text+".isspace())")
print(short_text.isspace())

print("# Check if string is Title", "==>", "print("+short_text+".istitle())")
print(short_text.istitle())

print("# make Title string", "==>", 'print(long_text.title())')
print(long_text.title())

print("#centering string with given padding", "==>",
      'print("########"+'+long_text+'.center(20)+"########")')
print("########"+long_text.center(20)+"########")

print("# Right justified string", "==>",
      'print("******"+short_text.rjust(20)+"******")')
print("******"+short_text.rjust(20)+"******")

print("# Left justified string", "==>",
      'print("******"+short_text.ljust(20)+"******")')
print("******"+short_text.ljust(20)+"******")

print("# fill string with leading zero", "==>", 'print(str(number).zfill(5))')
print(str(number).zfill(5))

print("# Length of string", "==>", 'print(len('+long_text+'))')
print(len(long_text))
print(long_text.__len__())

print("# Boolean", "==>", 'print(bool("True"))')
print(bool(1))
print(bool("True"))
print(bool([]))
print(bool({}))

print("# convert string to mutable array of byte")
print(bytearray(long_text, 'UTF-8'))

print("# convert string to immutable bytes",
      "==>", 'print(bytes(long_text, "UTF-8"))')
print(bytes(long_text, 'UTF-8'))

print("# String encoding to integer encoding", "==>", "print(ord('a'))")
int_enc = ord("a")
print(int_enc)

print("# Integer encoding to string encoding", "==>", "print(chr(ord('a')))")
print(chr(int_enc))

print("# Float", "==>", "print(float(12.05))")
print(float("12"))
print(float(12.05))

print("# Hashing string", "==>", "print(hash(long_text))")
print(hash(long_text))

print("# Identity of string", "==>", "print(id(long_text))")
print(id(long_text))

print("# Convert to integer", "==>", 'print(int("5"))')
print(int("5"))

print("# Slicing string")
s = slice(0, 20, 2)
print(long_text[s])

print("# detect type", "==>", "print(type(s))")
print(type(s))

print("# Date time string", "==>", "print(date_object)")
print(date_object)

print("# Escape qoutes", "==>", "print(\"He is 5'10\" Tall\")")
print("He is 5'10\" Tall")

print("# string Encoding", "==>", "short_text.encode(encoding='utf-8')")
encoded = short_text.encode(encoding='utf-8')
print(encoded)

print("# string Decoding", "==>", encoded, ".decode()")
decoded = encoded.decode()
print(decoded)

print("# ascii string (kinda json.stringify)",
      "==>", "print(ascii(long_text))")
print(ascii(long_text))
print(ascii(True))
print(ascii(1))
print(ascii(words))

print("printing NonEnglish Chars")
bengali = 'বর্ণ'.encode('utf-8')
print("Bytes:", bengali, "\nBengali:", bengali.decode('utf-8'),
      "\nIf you are seeing BOXs instead of text, you might need to install font for your terminal.")
