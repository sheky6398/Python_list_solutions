# Write a Python program to remove None value from a given list. Go to the editor
# Original list:
# [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None value from the said list:
# [12, 0, 23, -55, 234, 89, 0, 6, -12]

l = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
x = []
for i in l:
    if i!=None:
        x.append(i)
print(x)