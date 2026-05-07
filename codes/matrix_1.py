import random
n = int(input())

def matrix_init(n):
    return [[random.randint(0,n*n*10) for _ in range(n)] for _ in range(n)]

def print_matrix(matrix):
    for line in matrix :
        print(line)

A = matrix_init(n)
B = matrix_init(n)
C = matrix_init(n)

AB = [[0 for _ in range(n)] for _ in range(n)]
ABC = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        for k in range(n) :
            AB[i][j] += A[i][k] * B[k][j]

for i in range(n) :
    for j in range(n) :
        ABC[i][j] = AB[i][j] + C[i][j]


print_matrix(ABC)
