# key: value | keys must be unique 
# index can be any immutable obj (e.g. integer, string, tuple, etc)

genZ = {
    "fr": "for real",
    "buzzing": "uprising",
    "no cap": "no lies"
}

print(genZ)
print("length:", len(genZ))

# or
for i in genZ:
    print(i, end = " ")
print()


# fetching the keys
keys = list(genZ.keys())  # list() lists elements (keys)
print(keys)

# fetching the values by their index (here, index is string)
print(genZ["fr"])
print(genZ["buzzing"])
print(genZ["no cap"])

# or
for i in genZ:
    print(genZ[i], end = " ")
print()


# insert into the dictionary
genZ["ight"] = ["aight", "alright","all right"]
for i in genZ:
    print(genZ[i], end = " ")
print()