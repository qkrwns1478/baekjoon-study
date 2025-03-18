def tsp(dp, w, mask, pos, n):
    if mask == (1 << n) - 1:
        if w[pos][0] > 0:
            return w[pos][0]
        else:
            return float("inf")
    if dp[mask][pos] != -1:
        return dp[mask][pos]

    res = float("inf")
    for city in range(n):
        if mask & (1 << city) == 0 and w[pos][city]:
            res = min(res, w[pos][city] + tsp(dp, w, mask | (1 << city), city, n))

    dp[mask][pos] = res
    return res

n = int(input())
w = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    w[i] = list(map(int, input().split()))

dp = [[-1] * n for _ in range(1 << n)]
print(tsp(dp, w, 1, 0, n))