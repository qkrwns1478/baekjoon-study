import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
            if arr[x][y] > arr[nx][ny]:
                cnt += dfs(nx, ny)
    dp[x][y] = cnt       
    return dp[x][y]

dp = [[-1] * m for _ in range(n)]
dp[n-1][m-1] = 1
print(dfs(0, 0))