# Write a Python program to create a given flat list of all the keys in a flat dictionary. Go to the editor
# Sample Output:
# Original directory elements:
# {'Laura': 10, 'Spencer': 11, 'Bridget': 9, 'Howard ': 10}
# Flat list of all the keys of the said dictionary:
# ['Laura', 'Spencer', 'Bridget', 'Howard ']

l = {'Laura': 10, 'Spencer': 11, 'Bridget': 9, 'Howard ': 10}
x=[]
for i in zip(l):
    x.append(i)
print(x)