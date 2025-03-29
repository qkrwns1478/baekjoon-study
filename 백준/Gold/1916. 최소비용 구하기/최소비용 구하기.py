import sys
input = sys.stdin.readline
import heapq

def dij(s, e):
    queue = []
    heapq.heappush(queue, (0, s))
    dist[s] = 0

    while queue:
        now_dist, now = heapq.heappop(queue)

        if now == e:
            return

        if dist[now] < now_dist:
            continue

        for a, b in adj[now]:
            if now_dist+b < dist[a]:
                dist[a] = now_dist + b
                heapq.heappush(queue, (now_dist+b, a))

n = int(input())
m = int(input())

adj = dict()
for i in range(1, n+1):
    adj[i] = list()
    
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    #adj[b].append((a, c)) <- ???

#for i in range(1, n+1):
#    print(f"{i} : {adj[i]}")

s, e = map(int, input().split())

dist = [float("inf")] * (n+1)
dij(s, e)
print(dist[e])