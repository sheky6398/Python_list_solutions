# Write a Python program to find the indexes of all None items in a given list. Go to the editor
# Original list:
# [1, None, 5, 4, None, 0, None, None]
# Indexes of all None items of the list:
# [1, 4, 6, 7]

l = [1, None, 5, 4, None, 0, None, None]
x= []
y= []
for i in range(len(l)):
    if l[i] == None:
        x.append(i)
print(x)

#Another Method
for i,j in enumerate(l):
    if j==None:
        y.append(i)
print(x)