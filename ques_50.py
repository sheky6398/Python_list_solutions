#  Write a Python program to flatten a given nested list structure. Go to the editor
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

l = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
x = []
for i in l:
    if isinstance(i,list):
        x.extend(i)
    else:
        x.append(i)
print(x)