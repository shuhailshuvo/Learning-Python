import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)
if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")

string = 'hello 12 hi 89 Howdy 34'
pattern = '\d+'
result = re.findall(pattern, string)
print(result)

string = 'Twelve:12 Eighty nine:89 Thirty Four:34'
pattern = '\d+'
result = re.split(pattern, string)
print(result)


# multiline string
string = 'abc 12\
de 23 \n f45 6'
# matches all whitespace characters
pattern = '\s+'
# empty string
replace = ''
new_string = re.sub(pattern, replace, string)
print(new_string)

string = "Python is fun"
# check if 'Python' is at the beginning
match = re.search('\APython', string)
if match:
    print("pattern found inside the string", match)
else:
    print("pattern not found")
