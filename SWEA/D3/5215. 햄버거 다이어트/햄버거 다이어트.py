T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [[0] * (L+1) for _ in range(N+1)]
    for i in range(1, N+1):
        t, k = arr[i-1]
        for j in range(L+1):
            if k <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-k]+t)
            else:
                dp[i][j] = dp[i-1][j]

    print(f"#{tc} {dp[-1][-1]}")