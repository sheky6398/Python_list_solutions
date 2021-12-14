# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

a = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in a:
    if len(i)>2 and i[0]==i[-1]:
        count+=1
print(count)

#Another Method
def first_last(list):
    count = 0
    for i in list:
        if len(i)>2 and i[0]==i[-1]:
            count+=1
    return count
list = ['abc', 'xyz', 'aba', '1221']
print(first_last(list))

    