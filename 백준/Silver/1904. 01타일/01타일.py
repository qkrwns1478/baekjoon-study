import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
dp = [-1] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])