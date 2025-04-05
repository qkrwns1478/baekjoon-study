import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
for _ in range(m):
    s, e = map(int, input().split())
    queue = list()
    visited = set()
    queue.append((0, s))
    while queue:
        dist, node = heappop(queue)
        if node == e:
            break
        visited.add(node)
        for next_node, cost in adj[node]:
            if next_node not in visited:
                heappush(queue, (dist+cost, next_node))
    print(dist)