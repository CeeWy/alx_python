#!/usr/bin/python3
from add_0 import add

# Define a and b on separate lines
a = 1
b = 2

result = add(a, b)

print("{} + {} = {}\n".format(a, b, add(a, b)))