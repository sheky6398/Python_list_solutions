#  Write a Python program to remove duplicates from a list of lists. Go to the editor
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

l = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
x = []
for i in l:
    if i not in x:
        x.append(i)
print(x)