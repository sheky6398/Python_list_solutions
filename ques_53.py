#  Write a Python program to remove the K'th element from a given list, print the new list. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After removing an element at the kth position of the said list:
# [1, 1, 3, 4, 4, 5, 1]

l = [1, 1, 2, 3, 4, 4, 5, 1]
l.remove(2)
print(l)

#AnotherMethod
x = []
for i in l:
    if i!=2:
        x.append(i)
print(x)