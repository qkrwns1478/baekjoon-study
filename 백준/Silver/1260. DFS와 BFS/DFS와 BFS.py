import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(n+1):
    adj[i].sort()

def dfs(i):
    result.append(i)
    visited[i] = True
    
    for j in adj[i]:
        if not visited[j]:
            dfs(j)

visited = [False] * (n+1)
result = list()
dfs(v)
print(*result)

def bfs(i):
    queue = deque()
    queue.append(i)
    visited[i] = True
    while queue:
        now = queue.popleft()
        result.append(now)
        
        for j in adj[now]:
            if not visited[j]:
                visited[j] = True
                queue.append(j)

visited = [False] * (n+1)
result.clear()
bfs(v)
print(*result)