import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)] # (무게, 값)
#items.sort(key=lambda x: (x[0], -x[1]))

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = items[i-1]
    for j in range(k+1):
        '''if j - w >= 0:
            dp[i][j] = max(v, dp[i-1][j])
            if i > 1 and j - (items[i-2][0] + w) >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + v)'''
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

#for i in range(n):
#    print(dp[i])
print(dp[-1][-1])