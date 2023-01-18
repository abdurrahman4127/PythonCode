print("---------arithmatic operators---------")

print(7/3)  # float division
print(7//3) # integer division
print(7**2) # power

print("---------logical operators---------")

print(True and False) # &&
print(True or False)  # ||
print(not True)       # !

print("---------increment/decrement---------")

# pre/post-increment: 
# no i++, it's i = i + 1 or i += 1

i = 10
# i++ doesn't exist LOL!
i += 10
i = i + 10
print(i) # 30


print("---------special operators---------")

# 'is' and 'is not' check if variables of 2 objects refer 
# to the same address/object/memory location
print("type of True:", type(True))
print("type of None:", type(None))

x = True
print(x is None)
print(x is not None)
print(x is True)


print("---------membership operators---------")

str1 = "hello, world!"
print("hell" in str1)    # True if present
print("hey" not in str1) # True if not present