# Write a Python program to calculate the product of the unique numbers of a given list. Go to the editor
# Original List : [10, 20, 30, 40, 20, 50, 60, 40]
# Product of the unique numbers of the said list: 720000000

l = [10, 20, 30, 40, 20, 50, 60, 40]
x = []
mul = 1
for i in l:
    if i not in x:
        x.append(i)
for i in x:
    mul*=i
print(mul)


