# Write a Python program to convert list to list of dictionaries. Go to the editor
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
l,l2 = ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
x = []
for i,j in zip(l,l2):
    x.append({'color_name':i,'color_code':j})
print(x)


#Another Method
print([{'color_name':i,'color_code':j}for i in zip(l,l2)])
