
# Matrix Addition
matrix1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]
matrix2 = [[1,2,3],
        [4,5,6],
        [7,8,9]]

matrix3 = [[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

print(matrix3)
