#  Write a Python program to traverse a given list in reverse order, also print the elements with original index. Go to the editor
# Original list:
# ['red', 'green', 'white', 'black']
# Traverse the said list in reverse order:
# black
# white
# green
# red
# Traverse the said list in reverse order with original index:
# 3 black
# 2 white
# 1 green
# 0 red

l = ['red', 'green', 'white', 'black']
for i,j in reversed(list(enumerate(l))):
    print(i,j)