# Set Operations
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b))
print(a.intersection(b))
print(b.difference(a))
print(a.symmetric_difference(b))
a.update(b)
print(a)
a.clear()
print(a)
del a
