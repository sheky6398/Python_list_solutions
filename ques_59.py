# Write a Python program to find the list with maximum and minimum length. Go to the editor
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
# (3, [3, 5, 7])
# List with minimum length of lists:
# (1, [0])
# Original list:
# [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
# (4, [1, 34, 5, 7])
# List with minimum length of lists:
# (1, [12])


l = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
max_length = max(len(i) for i in l)
max_list = max(l, key = len)
print((max_length,max_list))
min_length = min(len(i) for i in l)
min_list = min(l,key=len)
print((min_length,min_list))

