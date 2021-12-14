# Write a Python program to clone or copy a list.

l = [1,2,3,4,1]
new_list = l
print(l)
print(new_list)

#Another Method
l = [1,2,3,4,1]
new_list = []
for i in l:
    new_list.append(i)
print(new_list)

#Another method
import copy
print(copy.deepcopy(l))