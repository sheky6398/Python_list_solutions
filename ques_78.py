#  Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings. Go to the editor
# Original list:
# [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings:
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']


l = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
x = []
y=  []
for i in l:
    if isinstance(i,int):
        x.append(i)
        x.sort()
    else:
        y.append(i)
        y.sort()
print(x+y)
