# Write a Python program to extract specified size of strings from a give list of string values. Go to the editor
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']

l = ['Python', 'list', 'exercises', 'practice', 'solution']
x = []
for i in l:
    if len(i)==6:
        x.append(i)
print(x)

# ANother Method
print([i for i in l if len(i)==6])