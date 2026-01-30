# List Comprehension
a = [1,2,3,4,5]
b = [x for x in a]
print(b)


a = [1,2,3,4,5,6,7,8,9]
even = [x for x in a if x%2 == 1]
print(even)

# Nested List Comprehension

# Flattening a matrix using loop
matrix = [[1,2,3],[4,5,6],[7,8,9]]
items = []
for i in matrix:
    for j in i:
        items.append(j)
print(items)

# Now by using List Comprehension
items = [j for i in matrix for j in i]
print(items)

