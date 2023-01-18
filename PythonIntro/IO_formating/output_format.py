# print(*object, sep = '', end = '\n', ...)

print("line 1")
print("line 2")

x = 10
print("value =", x)
print(f"value = {x}")


y = 20
print("value:", y)
print("value:", y, sep = '#')  # override 'space' with '#'


z = 30
print("value", end = ' = ') # ends with '='; not with '\n'
print(z) # end = '\t', t = tab


########################################################
val1, val2 = 10, 20

# print("val1 = {} and val2 = {}".format(val1, val2))
str1 = "val1 = {} and val2 = {}".format(val1, val2)
print(str1)

val3, val4 = 30, 40

# {1} and {2} get replaced by .format{x, y}
print("val3 = {0} and val4 = {1}".format(val3, val4))


val5, val6 = 50, 60

# .format{x = varX, y = varY}
print("val5 = {keyX} and val6 = {keyY}".format(keyX = val5, keyY = val6))


# format floating number:
# wrw = what you want your output to be replaced with
# #tnc = total number of character
# dap = how many (d)igit you want to (a)dd after (p)oint

# print("your_text: {:wrw#tnc.5f}".format(your_variable))

# e.g. total 8 digits; 5 digit after (.)
f1 = 3.1416
print("formatted value: {:08.5f}".format(f1))
print("formatted value: {key:08.5f}".format(key = f1))