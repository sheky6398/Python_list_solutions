# Reverse a list in Python
# Given:

# list1 = [100, 200, 300, 400, 500]

# [500, 400, 300, 200, 100]

list1 = [100, 200, 300, 400, 500]
x = []
for i in list1[::-1]:
    x.append(i)
print(x)