#  Write a Python program to scramble the letters of string in a given list. Go to the editor
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# After scrambling the letters of the strings of the said list:
# ['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']

import random

l = ['Python', 'list', 'exercises', 'practice', 'solution']
result = ["".join(random.sample(i,len(i))) for i in l]
print(result)
