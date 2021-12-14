# Write a Python program to multiply all the items in a list.
a=[1,2,3,5]
sum =1
for i in a:
    sum*=i
print(sum)

#Another Method
def mul(list):
    sum=1
    for i in list:
        sum*=i
    return sum
result = mul([1,2,3,5])
print(result)