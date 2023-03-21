str = "abcd efgh ijkl mnop qrst uvwx yz"
print("initially:", str)

# make it upper case
print(str.upper())

# make it lower case
print(str.lower())

# check for something in the string
if "0" in str: 
    print("present")
else: 
    print("absent")

# to find the index of something
print("index of 'z':", str.find("z"))


print("----------------------------------------------------")


str2 = "abcd7efgh7ijkl7mnop7qrst7uvwx7yz"
print("initially:", str2)

# to count the frequency of something
print(str2.count("7"))

# replace something with something
print(str2.replace("7", " "))

# split the string everywhere when 7 is found
print(str2.split("7"))   # creates a list 


print("----------------------------------------------------")


str3 = str2.split("7")
print("initially:", str3)

# beware, chap! join doesn't work on integer
print("".join(str3))    # joining by removing in-between space
print(" | ".join(str3))  #adding '|' ; adds " | " between two values