import sys
input = sys.stdin.readline

n, t = map(int, input().split())
arr = list()
for _ in range(n):
    k, s = map(int, input().split())
    arr.append((k, s))

dp = [[0] * (t+1) for _ in range(n+1)]
for i in range(1, n+1):
    k, s = arr[i-1]
    for j in range(t+1):
        if k <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k] + s)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][t])