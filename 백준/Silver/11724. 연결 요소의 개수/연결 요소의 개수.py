import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i):
    if i in visited:
        return

    visited.add(i)
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

#for i in range(1, n+1):
#    print(f"{i} : {adj[i]}")

answer = 0
visited = set()
for i in range(1, n+1):
    if i not in visited:
        dfs(i)
        answer += 1

print(answer)