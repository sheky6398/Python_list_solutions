# Write a Python program to remove duplicates from a list.

a = [10,20,30,20,10,50,60,40,80,50,40]
result = []
for i in a:
    if i not in result:
        result.append(i)
print(result)

#Another method
a = [10,20,30,20,10,50,60,40,80,50,40]
print(set(a))