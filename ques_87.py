# Write a Python program to get the items from a given list with specific condition. Go to the editor
# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Number of Items of the said list which are even and greater than 45
# 5

l = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
count = 0
for i in l:
    if i>45 and i%2==0:
        count+=1
print(count) 