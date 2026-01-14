N, S, M = map(int, input().split())
V = list(map(int, input().split()))

def verify(n):
    return 0 <= n <= M

dp = [[False for _ in range(M+1)] for _ in range(N+1)]
dp[0][S] = True

for i in range(1, N+1):
    for j in range(M+1):
        if dp[i-1][j]:
            if verify(j + V[i-1]):
                dp[i][j + V[i-1]] = True
            if verify(j - V[i-1]):
                dp[i][j - V[i-1]] = True

answer = -1
for i in range(M, -1, -1):
    if dp[-1][i]:
        answer = i
        break
# print(dp[-1])
print(answer)
