import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())
adj = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

# Prim 알고리즘
visited = [False] * (v+1)
min_heap = [(0, 1)]  # (가중치, 정점)
answer = 0

while min_heap:
    c, i = heapq.heappop(min_heap)
    
    if visited[i]:
        continue
    
    visited[i] = True
    answer += c
    
    for nc, j in adj[i]:
        if not visited[j]:
            heapq.heappush(min_heap, (nc, j))
            
print(answer)