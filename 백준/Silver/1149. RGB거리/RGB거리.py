import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]

for j in range(3):
    dp[0][j] = arr[0][j]

for i in range(1, n):
    for j in range(3):
        min_val = float("inf")
        for k in range(3):
            if k != j:
                min_val = min(min_val, dp[i-1][k] + arr[i][j])
        dp[i][j] = min_val

print(min(dp[-1]))