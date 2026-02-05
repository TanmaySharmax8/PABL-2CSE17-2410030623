#  You are given two arrays a[] and b[], return the Union of both the arrays in any order.
a= [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
c=[]
for i in a:
    if i not in c: c.append(i)
for i in b:
    if i not in c: c.append(i)
print(c)