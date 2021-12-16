# Write a Python program to remove duplicate words from a given list of strings. Go to the editor
# Original String:
# ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
# After removing duplicate words from the said list of strings:
# ['Python', 'Exercises', 'Practice', 'Solution']


l = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
x = []
for i in l:
    if i not in x:
        x.append(i)
print(x)
