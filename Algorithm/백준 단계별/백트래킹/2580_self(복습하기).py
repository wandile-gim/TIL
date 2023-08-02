sudoku = [list(map(int, input().split())) for _ in range(9)]

zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def ispromissing(x, y):
    promiss = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 행과 열 체크
    for i in range(9):
        if sudoku[x][i] in promiss:
            promiss.remove(sudoku[x][i])
        if sudoku[i][y] in promiss:
            promiss.remove(sudoku[i][y])

    x //= 3
    y //= 3
    for p in range(x*3, (x+1)*3):
        for q in range(y*3, (y+1)*3):
            if sudoku[p][q] in promiss:
                promiss.remove(sudoku[p][q])

    return promiss


def dfs(idx):

    if len(zeros) == idx:
        for row in sudoku:
            print(*row)
        return
    else:
        (x, y) = zeros[idx]
        promissing = ispromissing(x, y)

        for num in promissing:
            sudoku[x][y] = num
            dfs(idx+1)
            sudoku[x][y] = 0


dfs(0)
