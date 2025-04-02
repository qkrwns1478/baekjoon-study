import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = [list(input()) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(x, y, mode): 
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= n-1:
            if not visited[nx][ny]:
                if arr[x][y] == arr[nx][ny]:
                    dfs(nx, ny, mode)
                elif mode == 1 and arr[x][y] == "R" and arr[nx][ny] == "G":
                    dfs(nx, ny, mode)
                elif mode == 1 and arr[x][y] == "G" and arr[nx][ny] == "R":
                    dfs(nx, ny, mode)

ans1 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, 0)
            ans1 += 1
ans2 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, 1)
            ans2 += 1
print(ans1, ans2)