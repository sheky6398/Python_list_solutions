# Write a Python program to randomize the order of the values of an list, returning a new list. Go to the editor
# Sample Output:
# Original list: [1, 2, 3, 4, 5, 6]
# Shuffle the elements of the said list:
# [3, 2, 4, 1, 6, 5]

import random
l = [1, 2, 3, 4, 5, 6]
random.shuffle(l)
print(l)

