import random
n = int(input())

def matrix_init(n):
    return [[random.randint(0,n*n*10) for _ in range(n)] for _ in range(n)]

def print_matrix(matrix):
    for line in matrix :
        print(line)

A = matrix_init(n)
A_new = [list(rows) for rows in zip(*A)]

print_matrix(A_new)
