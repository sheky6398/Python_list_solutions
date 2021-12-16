# Write a Python program to remove empty lists from a given list of lists. Go to the editor
# Original list:
# [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
# After deleting the empty lists from the said lists of lists
# ['Red', 'Green', [1, 2], 'Blue']

l = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
x = []
for i in l:
    if i!=[]:
        x.append(i)

print(x)