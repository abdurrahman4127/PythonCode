import math

# anonymous / lambda function
# syntax: <lambda> <arguments>: <expression>

sayHello = lambda name: "hello, " + name
print(sayHello("world"))

add_num = lambda x, y: (x + y)
print(add_num(77, 33))

calc_square = lambda num: (num**2)
print(calc_square(7))


# ------------------------------------------------------------

# map() applies a given function to all items of an input list
# changes original value

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: (x**2), numbers)
square_rooted_numbers = map(lambda x: math.sqrt(x), numbers)

print(list(squared_numbers)) # Output: [1, 4, 9, 16, 25]
print(list(square_rooted_numbers)) # Output: [1, 4, 9, 16, 25]


# ---------------------------------------------------------------
# filter() filters the elements of an input iterable for which a given function returns True
# doesn't change original value

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: (x%2 == 0), numbers)
odd_numbers = filter(lambda x: (x%2 != 0), numbers)

print(list(even_numbers))
print(list(odd_numbers))