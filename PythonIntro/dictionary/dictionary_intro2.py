# special kinda list where index can be immutable too

dct = {
    # format: key/index: value 
    1: "value1",
    (2, 3, 4): "value2",
    "mykey": "value3"
}

# to access: dictionary_name[index]
print(dct[1])
print(dct[(2, 3, 4)])
print(dct["mykey"])


# insert into the dictionary; index must be unique
dct["another"] = "value4"
print(dct["another"])


# insert before checking with function
def check_key(key, value):
    if key in dct:
        print(f"key '{key}' is already available; can't insert")
    else:
        dct[key] = value
        print("successfully inserted")

check_key("another2", "value5")
print(dct["another2"])


# check for key... normally with "if <var> in <list>" value would be checked (here, key)
key = "random_key" 
if key in dct:
    print(f"yeah, '{key}' is present")
else:
    print(f"nah, '{key}' ain't present")  


# extract keys/values from dictionary
print(dct.keys())
print(dct.values())

# to see both
print(dct.items())

# <var> in dictionary_name iterates through the keys (not values) 
for key in dct:
    print(f"{key}: {dct[key]}")

# or
for (key,value) in dct.items():   # dct.items() contains both key and value
    print(key, " => ", value)


# copy dictionary; dict is mutable. change in one affects another if both refer to same location
dct2 = dct.copy()
dct2["another3"] = "value6"

# print(dct["another3"])  # change of 'dct2' didn't affect 'dct' 
print(dct2["another3"])


# to delete/remove
key = "another3"

# dct2.pop(key)
del dct2[key]

if key in dct2:
    print(f"yes, {key} is present")
else: 
    print(f"no, {key} is NOT present")

# to clear everything from the dictionary
dct2.clear()
print(dct2)   # returns empty dictionary, {}