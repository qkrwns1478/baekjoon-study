import sys

def remove_queen(i, j):
    for k in range(n):
        board[i][k] -= 1
        board[k][j] -= 1
        if i + k < n and j + k < n:
            board[i+k][j+k] -= 1
        if i - k >= 0 and j - k >= 0:
            board[i-k][j-k] -= 1
        if i + k < n and j - k >= 0:
            board[i+k][j-k] -= 1
        if i - k >= 0 and j + k < n:
            board[i-k][j+k] -= 1
            
def set_queen(i, j):
    for k in range(n):
        board[i][k] += 1
        board[k][j] += 1
        if i + k < n and j + k < n:
            board[i+k][j+k] += 1
        if i - k >= 0 and j - k >= 0:
            board[i-k][j-k] += 1
        if i + k < n and j - k >= 0:
            board[i+k][j-k] += 1
        if i - k >= 0 and j + k < n:
            board[i-k][j+k] += 1

def queen(i, j):
    global answer

    if board[i][j] > 0:
        return
    
    set_queen(i, j)
    
    if j+1 == n:
        answer += 1
        remove_queen(i, j)
        return

    for k in range(n):
        queen(k, j+1)
        
    remove_queen(i, j)
            
n = int(sys.stdin.readline())
answer = 0
board = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    queen(i, 0)
print(answer)