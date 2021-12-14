# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(l[1:4])

#Another Method
l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
result = []
for i in range(len(l)):
    if i in [0,4,5]:
        continue
    else:
        result.append(l[i])
print(result)

#Another Method
l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
result = []
for i in range(len(l)):
    if i not in [0,4,5]:
        result.append(l[i])
print(result)
