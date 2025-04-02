import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def bfs():
    queue = deque()
    tmp = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            tmp[i][j] = arr[i][j]
            if tmp[i][j] == 2:
                queue.append((i, j))
                
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    queue.append((nx, ny))

    global answer
    cnt = 0
    for i in range(n):
        cnt += tmp[i].count(0)
    answer = max(answer, cnt)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

wall(0)
print(answer)