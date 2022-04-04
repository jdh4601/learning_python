# variable
a = [1, 2, 3, 4]
a[2] = 5
print(a)

b = a[:]
b[2] = 6
print(b)


# copy
from copy import copy
c = [1, 2, 3, 4]
d = copy(c)
c[1] = 5
print(d)
