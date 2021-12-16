# Write a Python program to sum two or more lists, the lengths of the lists may be different. Go to the editor
# Original list:
# [[1, 2, 4], [2, 4, 4], [1, 2]]
# Sum said lists with different lengths:
# [4, 8, 8]
# Original list:
# [[1], [2, 4, 4], [1, 2], [4]]
# Sum said lists with different lengths:
# [8, 6, 4]

l = [[1, 2, 4], [2, 4, 4], [1, 2,1]]
x = []
for i in zip(*l):
    x.append(sum(i))
print(x)
