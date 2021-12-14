# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

new_list = []
for i in range(1,31):
    new_list.append(i**2)
print(new_list[:5]+new_list[25:])

#Another Method 
result = []
for i in range(31):
    if i>=1 and i<=5 or i>=25 and i<=30 :
        result.append(i**2)
print(result)