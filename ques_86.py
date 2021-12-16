# Write a Python program to find the maximum and minimum values in a given list of tuples. Go to the editor
# Original list with tuples:
# [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
# Maximum and minimum values of the said list of tuples:
# (78, 60)

l = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
x = []
for i in l:
    for j in i:
        if isinstance(j,int):
            x.append(j)
print((max(x),min(x)))
