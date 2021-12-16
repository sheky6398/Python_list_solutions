# Write a Python program to Zip two given lists of lists. Go to the editor
# Original lists:
# [[1, 3], [5, 7], [9, 11]]
# [[2, 4], [6, 8], [10, 12, 14]]
# Zipped list:
# [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]


l1 = [[1, 3], [5, 7], [9, 11]]
l2 = [[2, 4], [6, 8], [10, 12, 14]]
x = []
for i,j in zip(l1,l2):
    x.append(i+j)
print(x)



