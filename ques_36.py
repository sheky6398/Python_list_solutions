# Write a Python program to compute the difference between two lists. Go to the editor
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

color1, color2 = ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
diff1 = list(set(color1)-set(color2))
diff2 = list(set(color2)-set(color1))
print(diff1)
print(diff2)