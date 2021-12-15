# Write a Python program to find the second smallest number in a list.

l = [1, 2, -8, -2, 0, -2]
first_lar  = min(l)
l.remove(first_lar)
print(min(l))
    