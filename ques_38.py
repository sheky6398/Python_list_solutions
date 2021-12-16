# Write a Python program to convert a string to a list.


color ="['Red', 'Green', 'White']"
color1 = color.split()
for i in color1:
    print(i,end="")

#Another Method
print("".join(color1))