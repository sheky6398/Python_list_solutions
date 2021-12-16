# Write a Python program to access multiple elements of specified index from a given list.


nums = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
list_index = [0,3,5,7,10]
print([nums[i] for i in list_index])

#Another Method
x = []
for i in list_index:
    x.append(nums[i])
print(x)