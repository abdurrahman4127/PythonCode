str = "abcd efgh ijkl mnop qrst uvwx yz"
print("initially:", str)

# make it upper case
print(str.upper())

# make it lower case
print(str.lower())

# check for something in the string
if "0" in str: print("present")
else: print("absent")

# to find the index of something
print("index of 'z':", str.find("z"))


print("----------------------------------------------------")


str2 = "abcd7efgh7ijkl7mnop7qrst7uvwx7yz"
print("initially:", str2)

# to count the frequency of something
print(str2.count("7"))

# replace something with something
print(str2.replace("7", " "))

# split the string everywhere 7 if found
print(str2.split("7"))   # creates a list 


print("----------------------------------------------------")


str3 = str2.split("7")
print("initially:", str3)

# join the list by removing their in-between space
print("".join(str3))

# join the list by adding '|' ; adds " | " between two values
print(" | ".join(str3))