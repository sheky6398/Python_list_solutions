# Write a Python program to find the list of words that are longer than n from a given list of words.
str = "The quick brown fox jumps over the lazy dog"
n = 3
result = []
for i in str.split():
    if len(i)>n:
        result.append(i)
print(result)

#Another Method
def longer_list(n,str):
    for i in str.split():
        if len(i)>n:
            result.append(i)
        return result
print(longer_list(3,"The quick brown fox jumps over the lazy dog"))