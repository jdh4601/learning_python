# variable
a = [1, 2, 3, 4]
b = a
a[2] = 5
print(a)
print(b)
print(a is b)

# copy
from copy import copy
c = [1, 2, 3, 4]
d = copy(c)
c[1] = 5
print(d)
