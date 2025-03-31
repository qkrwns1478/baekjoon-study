import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
dist = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().strip().split())
    if dist[a][b] > c:
        dist[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == float("inf"):
            dist[i][j] = 0
    print(*dist[i][1:])