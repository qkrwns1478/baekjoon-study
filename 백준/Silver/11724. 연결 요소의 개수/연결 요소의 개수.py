import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i):
    if visited[i]:
        return

    visited[i] = True
    for j in adj[i]:
        dfs(j)

n, m = map(int, input().split())
adj = dict()
for i in range(1, n+1):
    adj[i] = list()
    
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    adj[u].sort()
    adj[v].sort()

answer = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)