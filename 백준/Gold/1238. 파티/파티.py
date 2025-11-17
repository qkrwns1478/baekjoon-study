from collections import defaultdict
from heapq import heappush, heappop

N, M, X = map(int, input().split())
d = defaultdict(list)
for _ in range(M):
    A, B, T = map(int, input().split())
    d[A].append((T, B))

INF = float("inf")
answer = 0

def dij(s, e):
    dist = [INF] * (N+1)
    dist[s] = 0
    hq = list()
    heappush(hq, (0, s))
    while hq:
        cur_dist, cur_node = heappop(hq)
        if cur_node == e:
            return cur_dist
        if dist[cur_node] < cur_dist:
            continue
        for nxt in d[cur_node]:
            nxt_dist, nxt_node = nxt
            cost = dist[cur_node] + nxt_dist
            if cost < dist[nxt_node]:
                dist[nxt_node] = cost
                heappush(hq, (cost, nxt_node))

for n in range(1, N+1):
    if n == X:
        continue
    cur = dij(n, X) + dij(X, n)
    answer = max(answer, cur)
print(answer)