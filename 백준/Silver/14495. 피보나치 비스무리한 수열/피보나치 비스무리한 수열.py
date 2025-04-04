n = int(input())
if n >= 3:
    dp = [0] * (n)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-3]
    print(dp[n-1])
else:
    print(1)