import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
arr = list()
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()

queue = []
for s, e in arr:
    if queue and queue[0] <= s:
        heappop(queue)
    heappush(queue, e)

print(len(queue))