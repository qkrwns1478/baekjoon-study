import sys
input = sys.stdin.readline
import heapq

v, e = map(int, input().split())
k = int(input())
dist= [float("inf")] * (v+1)
visited = [False] * (v+1)
arr = [[] for _ in range(v+1)]
queue = list()

for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

heapq.heappush(queue, (0, k))
dist[k] = 0

while queue:
    _, now = heapq.heappop(queue)
    
    if visited[now]:
        continue
    
    visited[now] = True
    for next, next_val in arr[now]:
        if dist[next] > dist[now] + next_val:
            dist[next] = dist[now] + next_val
            heapq.heappush(queue, (dist[next], next))
            
for i in range(1, v+1):
    if visited[i]:
        print(dist[i])
    else:
        print("INF")