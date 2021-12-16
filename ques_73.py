# Write a Python program to calculate the sum of the numbers in a list between the indices of a specified range. Go to the editor
# Original list:
# [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
# Range: 8 , 10
# Sum of the specified range:
# 29


l = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
x = []
for i in range(len(l)):
    if i>=8 and i<=10:
        x.append(l[i])
print(sum(x))