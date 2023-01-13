# explicit data conversion
num1 = 10
num2 = float(num1)
num3 = complex(num1)
str1 = str(num1)

print(f"num1 = {num1} | type:", type(num1))
print(f"num2 = {num2} | type:", type(num2))
print(f"num3 = {num3} | type:", type(num3))
print(f"str1 = {str1} | type:", type(str1))


# implicit data conversion
a1 = 4    # int
a2 = 3.7  # float
a3 = a1 + a2 #float
print(a3)


a4 = "3.7"
# print(a1 + a3) error
# print(a1 + int(a4)) error
print(a1 + float(a4)) # float