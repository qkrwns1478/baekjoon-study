import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
adj = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    s = list(input())
    for j in range(m):
        adj[i][j] = int(s[j])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if adj[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    adj[nx][ny] = adj[x][y] + 1
                    queue.append((nx, ny))

bfs(0, 0)
print(adj[n-1][m-1])