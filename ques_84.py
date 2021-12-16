#  Write a Python program to reverse a given list of lists. Go to the editor
# Original list:
# [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
# Reverse said list of lists:
# [['white', 'black', 'pink'], ['green', 'blue'], ['orange', 'red']]
# Original list:
# [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
# Reverse said list of lists:
# [[2, 3, 4, 2, 4], [0, 2, 4, 5], [1, 2, 3, 4]]

l = [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
x=[]
for i in reversed(l):
    x.append(i)
print(x)