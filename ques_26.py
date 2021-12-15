# Write a Python program to convert a list of multiple integers into a single integer. Go to the editor
# Sample list: [11, 33, 50]
# Expected Output: 113350
l = [11, 33, 50]

for i in l:
    print(i,end="")

#Another method
l = [11, 33, 50]
print(int("".join(map(str,l))))