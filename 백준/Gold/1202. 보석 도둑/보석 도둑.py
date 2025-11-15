from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
jewels = list()
bags = list()

for _ in range(N):
    jewels.append(tuple(map(int, input().split())))
for _ in range(K):
    bags.append(int(input()))

jewels.sort()
bags.sort()

total = 0
queue = list()
for i in range(K):
    while jewels and jewels[0][0] <= bags[i]:
        heappush(queue, -jewels[0][1])
        heappop(jewels)
    if queue:
        total += -heappop(queue)
print(total)