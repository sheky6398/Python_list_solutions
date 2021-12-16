# Write a Python program to concatenate element-wise three given lists. Go to the editor
# Original lists:
# ['0', '1', '2', '3', '4']
# ['red', 'green', 'black', 'blue', 'white']
# ['100', '200', '300', '400', '500']
# Concatenate element-wise three said lists:
# ['0red100', '1green200', '2black300', '3blue400', '4white500']
l1 = ['0', '1', '2', '3', '4']
l2 =  ['red', 'green', 'black', 'blue', 'white']
l3 =  ['100', '200', '300', '400', '500']
x= []
for i,j,k in zip(l1,l2,l3):
    x.append(i+j+k)
print(x)