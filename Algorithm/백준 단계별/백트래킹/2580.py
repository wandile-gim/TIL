sudoku = [list(map(int, input().split())) for _ in range(9)]

zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def is_promising(i, j):
    promising = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])

    # 3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])

    return promising


flag = False


def dfs(x):
    global flag

    if flag:  # 이미 답이 출력된 경우
        return

    if x == len(zeros):  # 마지막 0까지 다 채웠을 경우
        for row in sudoku:
            print(*row)
        flag = True  # 답 출력
        return

    else:
        (i, j) = zeros[x]
        promising = is_promising(i, j)

        for num in promising:
            sudoku[i][j] = num  # 유망한 숫자 중 하나를 넣어줌
            dfs(x + 1)  # 다음 0으로 넘어감
            sudoku[i][j] = 0


dfs(0)
