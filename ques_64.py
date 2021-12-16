#  Write a Python program to find the item with maximum occurrences in a given list. Go to the editor
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# Item with maximum occurrences of the said list:
# 2

l =  [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
dict = {}
for i in l:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
for i,j in sorted(dict.items(),key = lambda x:x[1],reverse=True)[:1]:
    print(i)