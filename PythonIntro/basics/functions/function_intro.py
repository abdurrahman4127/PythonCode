'''it's a good practice to add multi-line comment before starting - as documentation'''


# empty body function
def empty_body_func():
    pass  # write 'pass' is the function contains nothing

# prints 'None' since nothing is returned
print(empty_body_func())


# --------------------------------------------------


def function1(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"

# or
# for i in [1, -3, 4, 9, 0, -0]:
#     print(function1(i))

arr = [1, -3, 4, 9, 0, -0]
for i in arr:
    print(function1(i))


# -------------------------------------------------------


def function2(array):
    return (array + array)  # concat

print(function2(array=[10, 20, 30, 40]))

# arr = [10, 20, 30, 40]
# print(function2(arr))


# ------------------------------------------------------


# min-max
def min_max(arr):
    return min(arr), max(arr)

arr = [1, -3, 4, 9, 0, -0]
# print(min_max(arr))
minimum, maximum = min_max(arr) 
print(f"minimum: {minimum}\nmaximum: {maximum}")