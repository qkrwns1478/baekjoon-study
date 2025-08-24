import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
arr = list(tuple(map(int, input().split())) for _ in range(n))
arr.sort(key=lambda x: (x[0], -x[1]))

queue = []
heappush(queue, arr[0][1])

answer = 1
for i in range(1, n):
    s, e = arr[i]
    if s >= queue[0]:
        heappop(queue)
        heappush(queue, e)
        answer += 1
    else:
        heappush(queue, e)

print(answer)