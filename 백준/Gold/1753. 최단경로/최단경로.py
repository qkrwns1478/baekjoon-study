import sys
input = sys.stdin.readline
import heapq

v, e = map(int, input().split())
k = int(input())
arr = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

def dijkstra(arr, start):
    D = [float("inf")] * (v+1)
    D[start] = 0
    queue = [(0, start)]

    while queue:
        now_dist, now_node = heapq.heappop(queue)

        if now_dist > D[now_node]:
            continue

        for node, weight in arr[now_node]:
            cost = now_dist + weight
            if cost < D[node]:
                D[node] = cost
                heapq.heappush(queue, (cost, node))

    return D[1:]

result = dijkstra(arr, k)
for i in result:
    if i == float("inf"):
        print("INF")
    else:
        print(i)