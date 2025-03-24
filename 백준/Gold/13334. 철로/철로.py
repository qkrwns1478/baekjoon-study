import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    h, o = map(int, input().split())
    if h > o :
        h, o = o, h
    arr.append((h, o))
arr.sort(key=lambda x: x[1])
#print(arr)

d = int(input())
min_heap = list()
answer = 0

for h, o in arr:
    heapq.heappush(min_heap, h)
    #print(min_heap, o-d)

    while min_heap and min_heap[0] < o - d:
        heapq.heappop(min_heap)

    answer = max(answer, len(min_heap))
    #print(min_heap, answer)

#print("-" * 20)
print(answer)