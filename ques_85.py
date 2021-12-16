# Write a Python program to find the maximum and minimum values in a given list within specified index range. Go to the editor
# Original list:
# [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
# Index range:
# 3 to 8
# Maximum and minimum values of the said given list within index range:
# (5, 0)

l = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
x=[]
for i in range(len(l)):
    if i>=3 and i<=8:
        x.append(l[i])
print((max(x),min(x)))
