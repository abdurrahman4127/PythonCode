# tuple is immulable - can't change/update its elements
# > elements are presented inside ()

tpl = (1, 2, 3, 4, 5, 6, 7)

print(tpl)
print("lenght:", len(tpl))
print("6th index:", tpl[6])


# print with for loop
for i in tpl:
    print(i, end=" ")
print()


# print with slicing
print(tpl[0:4])
print(tpl[0:-1])


# access with comprehension 
square = [i**2 for i in tpl]
print("square:", square)


# check odd-even
odd_even = ["even" if i%2==0 else "odd" for i in tpl]
print(odd_even)


# can't remove/delete single element. if want to remove, remove all
del tpl
# print(tpl) # can't access