import sys
input = sys.stdin.readline

n, t = map(int, input().split())
arr = list()
total = 0
for _ in range(n):
    d, m = map(int, input().split())
    arr.append((d, m))
    total += m

dp = [[0] * (t+1) for _ in range(n+1)]
for i in range(1, n+1):
    d, m = arr[i-1]
    for j in range(t+1):
        if d <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-d] + m)
        else:
            dp[i][j] = dp[i-1][j]

print(total - dp[n][t])