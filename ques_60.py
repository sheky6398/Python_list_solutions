# Write a Python program to count the number of sublists contain a particular element. Go to the editor
# Original list:
# [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# Count 1 in the said list:
# 3
# Count 7 in the said list:
# 2
# Original list:
# [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# Count 'A' in the said list:
# 3
# Count 'E' in the said list:
# 1


l = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
count = 0
for i in l:
    for j in i:
        if j ==7:
            count+=1
print(count)