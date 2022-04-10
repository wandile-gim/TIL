def solution(board, moves):
    answer = []
    box = []
    for move in moves:
        move = move-1
        for i in range(len(board)):
            if board[i][move] != 0:
                item = board[i][move]
                board[i][move] = 0
                box.append(item)
                if box[-1:] == box[-2:-1]:
                    answer += box[-1:]
                    box = box[:-2]
                break

    return len(answer)*2
