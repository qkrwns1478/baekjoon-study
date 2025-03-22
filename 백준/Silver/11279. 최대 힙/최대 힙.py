import heapq
import sys
input = sys.stdin.readline

stack = list()
n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if not stack:
            print(0)
        else:
            print(-heapq.heappop(stack))
    else:
        heapq.heappush(stack, -x)