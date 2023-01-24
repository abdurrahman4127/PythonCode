lst = ["l lawliet", "spike spiegel", "simon riley", "abdur rahman"]

# length finding
length = [len(i) for i in lst]

# to iterate through the of lst 
iterate = 0 

for i in length:
    print(f"length of {lst[iterate]}: {i}")
    iterate += 1  # update to next index


# # or simply
# for i in range(0, len(lst)):
#     print(f"length of {lst[i]}: {length[i]}")

# # or 
# print(length)


# add strings before each item in the list
# add_str = [f"hlw, {i}" for i in lst]
add_str = ["hlw, " + i for i in lst]
print(add_str)