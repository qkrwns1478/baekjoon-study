import heapq
import sys
input = sys.stdin.readline

n = int(input())
min_heap = list()

for _ in range(n):
    heapq.heappush(min_heap, int(input()))

result = 0

while min_heap:
    try:
        a = heapq.heappop(min_heap)
        b = heapq.heappop(min_heap)
        result += a+b
        if min_heap:
            heapq.heappush(min_heap, a+b)
    except:
        break

print(result)