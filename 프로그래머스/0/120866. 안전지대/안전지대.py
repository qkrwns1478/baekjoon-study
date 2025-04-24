def solution(board):
    answer = 0
    n = len(board)
    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                board[i][j] = 1
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 0:
                            board[nx][ny] = 2
    for i in range(n):
        #print(*board[i])
        answer += board[i].count(0)
    return answer