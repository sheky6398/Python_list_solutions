# Write a Python program to split a list into different variables.
color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
for i in color:
    print(i)

#Another Method
a,b,c = color
print(a)
print(b)
print(c)