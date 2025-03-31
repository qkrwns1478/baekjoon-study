import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
            if arr[nx][ny] > 0 and not visited[nx][ny]:
                dfs(nx, ny)

n, m = map(int, input().strip().split())
arr = [[] * m for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().strip().split()))

year = 0
while True:
    flag = False
    cnt = 0 # 빙산 그룹 개수
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and not visited[i][j]:
                dfs(i, j)
                flag = True
                cnt += 1
    if not flag: # 다 녹을 때까지 빙하가 갈라지지 않으면
        break
    if cnt >= 2:
        break
    else:
        tmp = set()
        for i in range(n):
            for j in range(m):
                if arr[i][j] > 0:
                    melt = 0
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                            if arr[nx][ny] == 0:
                                melt += 1
                    if melt > 0:
                        tmp.add((i, j, melt))
        for i, j, melt in tmp:
            arr[i][j] -= melt
            if arr[i][j] < 0: arr[i][j] = 0
        year += 1
print(year if flag else 0)