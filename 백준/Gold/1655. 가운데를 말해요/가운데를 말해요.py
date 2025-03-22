import heapq
import sys
input = sys.stdin.readline

n = int(input())

max_heap = []
min_heap = []

m = int(input())
print(m)

for i in range(n-1):
    x = int(input())
    if x > m:
        heapq.heappush(min_heap, x)
        
        if len(max_heap) + 1 < len(min_heap):
            heapq.heappush(max_heap, -m)
            m = heapq.heappop(min_heap)
            
    else:
        heapq.heappush(max_heap, -x)
        
        if len(min_heap) < len(max_heap):
            heapq.heappush(min_heap, m)
            m = heapq.heappop(max_heap)
            m *= -1

    print(m)