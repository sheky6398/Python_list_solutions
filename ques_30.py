# Write a Python program to generate groups of five consecutive numbers in a list.
l = []
for i in range(5):
    for j in range(1,6):
        l.append(5*i+j)
print(l)

#ANother method
print([[5*i+j for j in range(1,6)] for i in range(5)])