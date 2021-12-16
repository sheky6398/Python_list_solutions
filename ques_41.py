#  Write a Python program to insert a given string at the beginning of all items in a list. Go to the editor
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4
l = [1,2,3,4]
x = []
for i in "emp".split():
    for j in l:
        x.append(i+str(j))
print(x)
#ANother Method
print([i+str(j) for j in l for i in "emp".split()])