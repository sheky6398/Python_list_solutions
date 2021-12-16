# Write a Python program to extract every first or specified element from a given two-dimensional list. Go to the editor
# Original list of lists:
# [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
# Extract every first element from the said given two dimensional list:
# [1, 4, 7]
# Extract every third element from the said given two dimensional list:
# [3, 6, 9]

l = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
print([i[1] for i in l])