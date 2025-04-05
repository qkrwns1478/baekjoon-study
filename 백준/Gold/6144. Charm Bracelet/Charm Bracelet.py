import sys
input = sys.stdin.readline

n, m = map(int, input().split())
charms = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (m+1)
for i in range(n):
    w, d = charms[i]
    for j in range(m, 0, -1):
        if w <= j:
            dp[j] = max(dp[j], dp[j-w] + d)
            
print(dp[-1])