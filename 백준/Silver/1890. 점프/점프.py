n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        v = arr[i][j]
        if v > 0:
            di = [v, 0]
            dj = [0, v]
            for k in range(2):
                ni = i + di[k]
                nj = j + dj[k]
                if ni <= n-1 and nj <= n-1:
                    dp[ni][nj] += dp[i][j]
print(dp[-1][-1])