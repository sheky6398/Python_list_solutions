# Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.

# Given:

# list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output:

# [5, 15, 25, 50]

list1 = [5, 20, 15, 20, 25, 50, 20]
x = []
for i in list1:
    if i == 20:
        continue
    else:
        x.append(i)
print(x)
