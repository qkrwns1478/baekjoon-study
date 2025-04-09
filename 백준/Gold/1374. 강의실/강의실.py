import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
arr = list()
for _ in range(n):
    _, b, c = map(int, input().split())
    arr.append((b, c))
arr.sort()

queue = []
for s, e in arr:
    if queue and queue[0] <= s:
        heappop(queue)
    heappush(queue, e)

print(len(queue))