# Write a Python program to remove the specific item from a given list of lists. Go to the editor
# Original list of lists:
# [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
# Remove 1st list from the saod given list of lists:
# [['Maroon', 'Yellow', 'Olive'], ['#800000', '#FFFF00', '#808000'], ['rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
# Remove 2nd list from the saod given list of lists:
# [['Red', 'Yellow', 'Olive'], ['#FF0000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
# Remove 4th list from the saod given list of lists:
# [['Red', 'Maroon', 'Yellow'], ['#FF0000', '#800000', '#FFFF00'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)']]

l = [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
n = 0
x = []
for i in l:
    x.append(i[:-1])
print(x)
    

