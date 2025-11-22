N = int(input())
arr = list(tuple(map(int, input().split())) for _ in range(N))
dp = [0] * N
max_val = 0

for i in range(N):
    for j in range(i+1):
        if j + arr[j][0] - 1 == i:
            dp[i] = max(dp[i], dp[i-arr[j][0]] + arr[j][1])
        dp[i] = max(max_val, dp[i])
        max_val = max(max_val, dp[i])

print(dp[-1])