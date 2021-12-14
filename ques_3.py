# Write a Python program to get the largest number from a list.
a = [1,2,3,4,67,2,99]
print(max(a))


#Another Method
result = sorted(a,reverse=True)[0]
print(result)