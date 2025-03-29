import sys
input = sys.stdin.readline
import heapq

n, m, k, x = map(int, input().split())

adj = dict()
for i in range(1, n+1):
    adj[i] = list()
    
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append((b, 1))

dist = [float("inf")] * (n+1)

def dij(s):
    queue = list()
    heapq.heappush(queue, (0, s))
    dist[s] = 0

    while queue:
        now_dist, now = heapq.heappop(queue)

        if dist[now] < now_dist:
            continue

        for a, b in adj[now]:
            if now_dist + b < dist[a]:
                dist[a] = now_dist + b
                heapq.heappush(queue, (now_dist + b, a))
dij(x)

answer = list()
for i in range(1, n+1):
    if dist[i] == k:
        answer.append(i)
if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)