from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)

N = int(input())
G = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

dp = [[1, 0] for _ in range(N+1)]
visited = [False] * (N+1)

def dfs(x):
    visited[x] = True
    for i in G[x]:
        if not visited[i]:
            dfs(i)
            dp[x][1] += dp[i][0]
            dp[x][0] += min(dp[i][0], dp[i][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))
