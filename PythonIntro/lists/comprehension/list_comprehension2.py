lst = [1, 2, 3, 4, 5, 6, 7]

even = ["even" for i in lst if i%2==0]
print("even:", even)

odd = ["odd" for i in lst if i%2!=0]
print("odd:", odd)


# if True, go left; else go right
ans = [f'{i} is even' if (i%2==0) else f'{i} is odd' for i in lst]
print(ans)