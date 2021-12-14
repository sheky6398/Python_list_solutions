# Write a Python program to get the difference between the two lists. 

l1 = [1, 3, 5, 7, 9]
l2 = [1, 2, 4, 6, 7, 8]
diff_1 = list(set(l1)-set(l2))
diff_2 = list(set(l2)-set(l1))
print(diff_1+diff_2)