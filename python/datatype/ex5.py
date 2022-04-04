# set
s1 = set([1, 2, 3])
s1.add(4)
print(s1.update([5, 6, 7]))
s1.remove(4)
print(s1)

L = [1, 2, 3, 3, 4, 4]
newList = list(set(L))
print(newList)

ex = set('hello')
print(ex)

set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

# intersection
print(set1 & set2)
print(set1.intersection(set2))

# union
print(set1 | set2)
print(set1.union(set2))

# difference
print(set1 - set2)
print(set1.difference(set2))

