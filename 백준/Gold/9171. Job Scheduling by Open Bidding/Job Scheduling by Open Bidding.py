import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    items = list()
    for i in range(n):
        a, b = input().split()
        items.append((int(a), float(b)))
    k = int(input())

    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        w, p = items[i-1]
        for j in range(k+1):
            if w <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + p)
            else:
                dp[i][j] = dp[i-1][j]

    time = dp[-1].index(max(dp[-1]))
    print("Problem {0}: {1} seconds scheduled for ${2:.2f}".format(t+1, time, dp[-1][time]))