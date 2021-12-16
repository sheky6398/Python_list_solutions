# Write a Python program to create the largest possible number using the elements of a given list of positive integers. Go to the editor
# Original list:
# [3, 40, 41, 43, 74, 9]
# Largest possible number using the elements of the said list of positive integers:
# 9744341403
# Original list:
# [10, 40, 20, 30, 50, 60]
# Largest possible number using the elements of the said list of positive integers:
# 605040302010
# Original list:
# [8, 4, 2, 9, 5, 6, 1, 0]
# Largest possible number using the elements of the said list of positive integers:
# 98654210

l = [8, 4, 2, 9, 5, 6, 1, 0]
for i in sorted(l,reverse=True):
    print(i,end="")