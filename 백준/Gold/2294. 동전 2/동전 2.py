n, k = map(int, input().split())
coin = list()
coin.append(0)
for _ in range(n):
    coin.append(int(input()))
dp = [[float("inf")] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    c = coin[i]
    for j in range(1, k+1):
        if j >= c:
            if j % c == 0:
                dp[i][j] = min(dp[i-1][j], j//c, dp[i][j-c] + 1)
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-c] + 1)
        else:
            dp[i][j] = dp[i-1][j]

if dp[n][k] == float("inf"):
    print(-1)
else:
    print(dp[n][k])