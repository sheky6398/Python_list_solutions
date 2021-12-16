# Write a Python program to remove duplicate dictionary from a given list. Go to the editor
# Original list with duplicate dictionary:
# [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
# After removing duplicate dictionary of the said list:
# [{'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]

l = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
x = []
for i in l:
    if i not in x:
        x.append(i)
print(x)