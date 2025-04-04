import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if visited[x][y]:
        return visited[x][y]
    
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= n-1:
            if arr[x][y] < arr[nx][ny]:
                dfs(nx, ny)
                visited[x][y] = max(visited[x][y], visited[nx][ny]+1)

answer = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            answer = max(answer, visited[i][j])

print(answer)