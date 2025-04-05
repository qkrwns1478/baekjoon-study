import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(k)]

dp = [[0] * (n+1) for _ in range(k+1)]

for i in range(1, k+1):
    I, T = arr[i-1]
    for j in range(n+1):
        if T <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-T] + I)
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[-1][-1])