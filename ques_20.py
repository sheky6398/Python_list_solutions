# Write a Python program to flatten a shallow list.



original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_list = []
for i in original_list:
    new_list.extend(i)
print(new_list)