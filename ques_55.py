# Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list. Go to the editor
# Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# Result:
# 243
 

l = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
length  = len(l)

print(sum(list(map(round,l))* length))

#Another Method
sum = 0
for i in l:
    sum+=round(i)
print(sum*length)


