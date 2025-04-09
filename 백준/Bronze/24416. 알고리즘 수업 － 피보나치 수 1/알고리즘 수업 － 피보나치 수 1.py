n = int(input())
dp = [0] * (n+1)
dp[4] = 3
dp[5] = 5
for i in range(6, n+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[n], n-2)