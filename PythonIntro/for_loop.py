# format: range(start, end, increment)

for i in range(7):
    print(i, end = " ")
print()


for i in range(2, 7):  # 7 isn't included
    print(i, end = " ")
print()


for i in range(7, 77, 10):
    print(i, end = " ")
print()


# in reverse order
for i in range(7, 0, -1):
    print(i, end = " ")
print()


# iterate through strings
name = "spike"
for i in name:
    print(i)

for i in "spiegel":
    print(i)


# iterate through object
shrek = ["shrek", "fiona", "donkey", "puss"]
for i in shrek:
    print(i, len(i), end = "\n")