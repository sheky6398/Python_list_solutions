# Write a Python program to select the odd items of a list.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = []
for i in x:
    if not i%2==0:
        l.append(i)
print(l)

#ANother Method
print([i for i in x if not i%2==0])

#ANother Method
print(x[::2])