lst = []

for i in range(9) :
    line = list(map(int, input().split()))
    lst.append(line)

def is_valid(x, y, k):
    for i in range(9) :
        if lst[i][x] == k :
            return False

    for i in range(9) :
        if lst[y][i] == k :
            return False

    x_start = (x // 3) * 3
    y_start = (y // 3) * 3

    for i in range(y_start, y_start + 3) :
        for j in range(x_start, x_start + 3) :
            if lst[i][j] == k :
                return False
    return True

def solve_sudoku():
    for i in range(9):
        for j in range(9):
            if lst[i][j] == 0:
                for k in range(1, 10):
                    if is_valid(j, i, k):
                        lst[i][j] = k
                        if solve_sudoku():
                            return True
                        lst[i][j] = 0
                return False
    return True

solve_sudoku()

for i in range(9) :
    for j in range(9) :
        print(lst[i][j], end = " ")
    print()
