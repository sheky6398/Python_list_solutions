# Write a Python program to convert a given list of strings into list of lists. Go to the editor
# Original list of strings:
# ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:
# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]

l = ['Red', 'Maroon', 'Yellow', 'Olive']
print([list(i) for i in l])