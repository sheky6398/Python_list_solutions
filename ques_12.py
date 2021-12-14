# Write a Python function that takes two lists and returns True if they have at least one common member.


def check(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                return True
            else:
                return False
l1=[2,3,1]
l2=[2,7,8]
print(check(l1,l2))


