import sys
input = sys.stdin.readline

n, m = map(int, input().split())
D = [[float("inf")] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    D[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    D[a][b] = 1
    D[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]

answer = 0
min_val = float("inf")
for i in range(1, n+1):
    tmp = sum(D[i][j] for j in range(1, n+1))
    if min_val > tmp:
        min_val = tmp
        answer = i

print(answer)