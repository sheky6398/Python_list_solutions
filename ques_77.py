# Write a Python program to find a first even and odd number in a given list of numbers. Go to the editor
# Original list:
# [1, 3, 5, 7, 4, 1, 6, 8]
# First even and odd number of the said list of numbers:
# (4, 1)


l = [1, 3, 5, 7, 4, 1, 6, 8]
x= []
y= []
for i in l:
    if i%2==0:
        x.append(i)
print(x[0])
for i in l:
    if i%2!=0:
        y.append(i)
print(y[0])
print((x[0],y[0]))
        
