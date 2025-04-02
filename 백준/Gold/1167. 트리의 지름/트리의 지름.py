import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

v = int(input())
adj = [[] for _ in range(v+1)]
for _ in range(v):
    queries = deque(map(int, input().split()))
    a = queries.popleft()
    while len(queries) > 1:
        b = queries.popleft()
        c = queries.popleft()
        adj[a].append((b,c))

def dfs(i, dist):
    global max_node
    global max_dist
    
    #print(i, end=" → ")
    if dist > max_dist:
        max_node = i
        max_dist = dist
        
    for j, cost in adj[i]:
        if not visited[j]:
            visited[j] = True
            dfs(j, dist + cost)

max_node = 0
max_dist = 0

visited = [False] * (v+1)
visited[1] = True
dfs(1, 0)
#print(max_dist)

visited = [False] * (v+1)
visited[max_node] = True
dfs(max_node, 0)

print(max_dist)