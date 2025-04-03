import sys
input = sys.stdin.readline

dx = [1, -1]
dy = [1, -1]
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def floor(x, y):
    visited[x][y] = True
    if arr[x][y] == "-":
        for i in range(2):
            ny = y + dy[i]
            if 0 <= ny <= m-1 and not visited[x][ny] and arr[x][ny] == arr[x][y]:
                floor(x, ny)
    else:
        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx <= n-1 and not visited[nx][y] and arr[nx][y] == arr[x][y]:
                floor(nx, y)

answer = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            floor(i, j)
            answer += 1
print(answer)