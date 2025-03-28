import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i):
    visited[i] = True

    for j in range(1, n+1):
        if not visited[j] and adj[i][j]:
            dfs(j)

n, m = map(int, input().split())
adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = 1
    adj[v][u] = 1

answer = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        if not adj[i]:
            answer += 1
            visited[i]
        else:
            dfs(i)
            answer += 1

print(answer)