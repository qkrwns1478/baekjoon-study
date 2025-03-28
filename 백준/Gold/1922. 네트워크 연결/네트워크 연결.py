import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

visited = [False] * (n+1)
min_heap = [(0, 1)]
answer = 0

while min_heap:
    com = heapq.heappop(min_heap)
    
    if visited[com[1]]:
        continue
    
    visited[com[1]] = True
    answer += com[0]
    
    for a, b in adj[com[1]]:
        if not visited[b]:
            heapq.heappush(min_heap, (a, b))
            
print(answer)