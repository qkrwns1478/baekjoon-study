import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
#for i in range(n):
#    print(arr[i])
dp = [[0] * n for _ in range(n)]
dp[0][0] = arr[0][0]
for i in range(n-1):
    for j in range(i+1):
        if dp[i+1][j] < dp[i][j] + arr[i+1][j]:
            dp[i+1][j] = dp[i][j] + arr[i+1][j]
        if dp[i+1][j+1] < dp[i][j] + arr[i+1][j+1]:
            dp[i+1][j+1] = dp[i][j] + arr[i+1][j+1]
#for i in range(n):
#    print(dp[i])
print(max(dp[-1]))