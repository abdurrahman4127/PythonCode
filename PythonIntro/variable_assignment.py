# single variable assignment
var1 = 10
print(var1)

# update
var1 = 20
print(var1)

# assign same value to different variable
var5 = var6 = var7 = "5, 6, and 7 have the same value"
print(var5)
print(var6)
print(var7)


# multi-variable assignment
var2, var3, var4 = 30, 40.5, "this is something else"
print(var2, var3, var4)


# type of variable, everything in python is object that referes to other obj
print("value of var2:", var2, "is of", type(var2))
print(f"value of var3: ${var3} is of", type(var3))
print("value of var4:", var4, "is of", type(var4))