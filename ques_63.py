# Write a Python program to count integer in a given mixed list. Go to the editor
# Original list:
# [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of integers in the said mixed list:
# 6


l = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
count = 0
for i in l:
    if isinstance(i,int):
        count+=1

print(count)
        

