import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(i):
    if i not in visited:
        visited.add(i)
        result_dfs.append(i)
        for j in adj[i]:
            dfs(j)

def bfs(i):
    queue = deque([i])
    visited = set()
    visited.add(i)
    result = list()

    while queue:
        node = queue.popleft()
        result.append(node)
        for j in adj[node]:
            if j not in visited:
                visited.add(j)
                queue.append(j)

    print(*result)
    del result
        

n, m, v = map(int, input().split())
adj = dict()
for i in range(1, n+1):
    adj[i] = list()
    
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    adj[a].sort()
    adj[b].sort()

#for i in range(1, n+1):
#    print(f"{i} : {adj[i]}")

visited = set()
result_dfs = list()
dfs(v)
print(*result_dfs)
del result_dfs

bfs(v)