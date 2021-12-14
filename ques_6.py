# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = []
for i in sorted(a,key=lambda x:x[1]):
    result.append(i)
print(result)

#Another method
def check(a):
    result = []
    for i in sorted(a,key=lambda x:x[0]):
        result.append(i)
    return result
print(check(a))