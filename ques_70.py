# Write a Python program to find the maximum and minimum product from the pairs of tuple within a given list. Go to the editor
# The original list, tuple :
# [(2, 7), (2, 6), (1, 8), (4, 9)]
# Maximum and minimum product from the pairs of the said tuple of list:
# (36, 8)

l = [(2, 7), (2, 6), (1, 8), (4, 9)]
x = []
for i,j in l:
    x.append(i*j)
print((max(x),min(x)))
