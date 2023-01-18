# module file: module_name.py
# > a single python file (unlike package)
# > contains python definitions & statements

# importing 'math' module
import math
print(math.pi)

# using alias
import math as m
print(m.pi)


# import everything from 'math' module (avoid; good practice)
# if everything is imported from math module, 
# then no need to access through module_name.
from math import *
print(pi) 

# using alias 
from math import pi as p
print(p)


# single operation can be imported
from math import sqrt
print(sqrt(7))

# multiple operations can be imported too
from math import pi, sqrt
print(pi)
print(sqrt(7))


# function to find out which name a module defines
# print(dir(math)) 

# or in a better way
for i in dir(math):
    print(i, end="\n")

# check if a function is in the module
func = "sqrt"
# func = "abs"
if func in dir(math):
    print(f"{func} is AVAILABLE in this module")
else:
    print(f"{func} is UNAVAILABLE in this module")


# without argument, dir() lists the currently defines ones
print(dir())