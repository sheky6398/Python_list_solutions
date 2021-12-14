# Write a Python program to print the numbers of a specified list after removing even numbers from it.

l = [7,8, 120, 25, 44, 20, 27]
result = []
for i in l:
    if not i%2==0:
        result.append(i)
print(result)

#ANother method
new_list = [i for i in l if not i%2==0]
print(new_list)