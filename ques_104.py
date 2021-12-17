# Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Expected output:

# ["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
x = []
for i in list1:
    if i== "":
        continue
    else:
        x.append(i)
print(x)