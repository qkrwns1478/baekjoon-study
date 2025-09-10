import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
queue = list()

tmp = list(map(int, input().strip().split()))
for i in tmp:
    heappush(queue, i)
for _ in range(n-1):
    tmp = list(map(int, input().strip().split()))
    for i in tmp:
        heappush(queue, i)
        heappop(queue)

print(heappop(queue))