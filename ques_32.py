# Write a Python program to insert an element before each element of a list

color = ['Red', 'Green', 'Black']
l=[]
for i in color:
    for j in ("c",i):
        l.append(j)
print(l)


#Another Method
print([j for j in ("c",i) for i in color ])




