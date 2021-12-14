# Write a Python program to sum all the items in a list.
a=[1,2,-8]
sum=0
for i in a:
    sum+=i
print(sum)


#Another Method 
def sum_(list):
    sum=0
    for i in list:
        sum+=i
    return sum
result = sum_([1,2,-8])
print(result)