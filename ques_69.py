# Write a Python program to reverse strings in a given list of string values. Go to the editor
# Original lists:
# ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

l = ['Red', 'Green', 'Blue', 'White', 'Black']
x = []
for i in l:
    x.append(i[::-1])
print(x)