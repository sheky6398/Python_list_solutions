# Write a Python program to extend a list without append. Go to the editor
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]
a,b = [10, 20, 30],[40, 50, 60]
print(a+b)

#Another Method
a.extend(b)
print(a)