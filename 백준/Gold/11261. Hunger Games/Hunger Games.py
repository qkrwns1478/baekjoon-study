import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    W = list(map(int, input().split()))
    P = list(map(int, input().split()))
    items = list()
    for i in range(n):
        items.append((W[i], P[i]))

    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        w, p = items[i-1]
        for j in range(k+1):
            if w <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + p)
            else:
                dp[i][j] = dp[i-1][j]
                
    print(dp[-1][-1])