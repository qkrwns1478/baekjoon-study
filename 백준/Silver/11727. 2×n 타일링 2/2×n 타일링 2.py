n = int(input())

dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    if i % 2 == 1:
        dp[i] = (dp[i-1] * 2 - 1) % 10007
    else:
        dp[i] = (dp[i-1] * 2 + 1) % 10007
print(dp[n])

#for i in range(3, n+1):
#    dp[i] = ((dp[i-1] - dp[i-2]) * dp[i-2] + dp[i-1]) % 10007
#print(dp[n])

# 1 : 1
# 2 : 3
# 3 : 5
# 4 : 11