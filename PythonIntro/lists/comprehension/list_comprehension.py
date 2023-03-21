# format: [<your_output> for <variable> in <your_list>]

# print length of values in a list
str1 = ["l", "spike", "partic", "simon"]
length = [len(i) for i in str1]
print(length)


# square of a list 
numbers = [1, 2, 3, 4, 5]
squared_numbers = [i**2 for i in numbers]
print(squared_numbers) 


# even checking 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [i for i in numbers if (i%2 == 0)]
print(even_numbers)


# sum of all values in the list
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sm = sum([i for i in num])
print("ans:", sm)

# prints all pairs
listA, listB = [1, 2, 3], [4, 5, 6] 
pairs = [(i, j) for i in listA for j in listB]
print(pairs) 

# it actually is: 
listA, listB = [1, 2, 3], [4, 5, 6] 

pairs = []
for i in listA:
    for j in listB:
        pairs.append((i, j))
print(pairs) 