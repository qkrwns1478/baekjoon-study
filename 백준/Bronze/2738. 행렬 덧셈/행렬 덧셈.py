n, m = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
b = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(n):
    b[i] = list(map(int, input().split()))
    
c = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        c[i][j] = a[i][j] + b[i][j]
    print(*c[i])