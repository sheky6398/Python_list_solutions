# Write a Python program to remove all strings from a given list of tuples. Go to the editor
# Original list:
# [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
# Remove all strings from the said list of tuples:
# [(100,), (80,), (90,), (88, 89), (90, 92)]

l = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
x = []
for i in l:
    for j in i:
        if isinstance(j,int):
            x.append([j])
print(x)