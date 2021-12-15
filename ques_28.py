#  Write a Python program to find missing and additional values in two lists. Go to the editor
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h

list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
diff = (set(list1)-set(list2))
diff2 = set(list2)-set(list1)
print('Missing values in second list: ',diff)
print('Additional values in second list: ',diff2)
