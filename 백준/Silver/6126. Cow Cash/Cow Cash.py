import sys
input = sys.stdin.readline

v, n = map(int, input().split())
arr = list()
for _ in range(v):
    arr.append(int(input()))
dp = [0] * (n+1)
dp[0] = 1

for i in arr:
    for j in range(i, n+1):
        # dp[j] : j 금액을 만들 수 있는 경우의 수
        dp[j] += dp[j-i]
            
print(dp[n])