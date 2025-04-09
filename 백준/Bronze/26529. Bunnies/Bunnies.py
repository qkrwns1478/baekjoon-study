n = int(input())
for _ in range(n):
    x = int(input())
    if x <= 1:
        print(1)
    else:
        dp = [0] * (x+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, x+1):
            dp[i] = dp[i-2] + dp[i-1]
        print(dp[x])