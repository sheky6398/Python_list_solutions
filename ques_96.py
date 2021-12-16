# Write a Python program to sort a given positive number in descending/ascending order. Go to the editor
# Descending -> Highest to lowest.
# Ascending -> Lowest to highest
# Original Number: 134543
# Descending order of the said number: 544331
# Ascending order of the said number: 133445
# Original Number: 43750973
# Descending order of the said number: 97754330
# Ascending order of the said number: 3345779

n = 134543
print(int(''.join(sorted(str(n),reverse=True))))
print(int(''.join(sorted(str(n)))))