# define a list
my_list = [4, 7, 0, 3]

my_iter = iter(my_list)
print("# get an iterator using iter()\n",
      "\titer([4, 7, 0, 3])\n\t", my_iter, "\n")


print("# iterate through it using next()",
      "next(my_iter) => 4 =>", next(my_iter))

print("# iterate through it using next()",
      "next(my_iter) => 7 =>", next(my_iter))

print("# iterate through it using next()",
      "next(my_iter) => 0 =>", next(my_iter))

print("# iterate through it using my_iter.__next__()",
      "next(my_iter) => 3 =>", next(my_iter))

# identify power of 2


class PowTwo:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


power = iter(PowTwo(5))
print(next(power))
print(next(power))
print(next(power))
print(next(power))
print(next(power))
print(next(power))
