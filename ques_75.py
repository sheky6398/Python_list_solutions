#  Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers. Go to the editor
# Original list:
# [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
# Index positions of the maximum value of the said list:
# 7
# Index positions of the minimum value of the said list:
# 3

l = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
# min_value = (map(max,i) for i in l)
# print(min_value)
x = []
max_value = max(l)
min_value = min(l)
for i in range(len(l)):
    if l[i]==max_value:
        print(i)
for i in range(len(l)):
    if l[i]==min_value:
        print(i)

# ANother Method
# Enumerate functions return index position and value thatswhy we use enumerate 

for i,j in enumerate(l):
    if j==max_value:
        print(i)

for i,j in enumerate(l):
    if j==min_value:
        print(i)

