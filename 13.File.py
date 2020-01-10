# seek() move the pointer to given position

# Read whole file in text
with open("Files/sample.txt", encoding='utf-8') as f:
    whole = f.read()
    print("complete File", whole)

# Read line
with open("Files/sample.txt", encoding='utf-8') as f:
    f.seek(200)
    line = f.readline()
    print(line)

# read file in loop
with open("Files/sample.txt", encoding='utf-8') as f:
    for line in f:
        print(" => ", line)

# Read file position
with open("Files/sample.txt", "r", encoding='utf-8') as f:
    print("Position: ", f.tell())
    f.readline()
    print("Position: (2nd line)", f.tell())
    f.readline()
    print("Position: (3rd line)", f.tell())

# Replace file contents
with open("Files/sample.txt", "w",  encoding='utf-8') as f:
    f.write("Completely new content\n")
    f.write("Second line\n")

# append with  file contents
with open("Files/sample.txt", "r+",  encoding='utf-8') as f:
    f.read()  # important to move the pointer
    f.write("\nnew line added\n")

# Clear file data
with open("Files/sample.txt", "r+",  encoding='utf-8') as f:
    print(f.truncate())

# read lines
with open("Files/sample.csv", "r",  encoding='utf-8') as f:
    book = f.readlines()
    book[10] = "000,FL,CLAY COUNTY,705600,705600,705600,705600,705600,1010842.56,14112,35280,0,0,30.100628,-81.703751,Residential,Masonry,1"
    print(book[10])

# and write everything back
with open('Files/sample.csv', 'w') as file:
    file.writelines(book)
