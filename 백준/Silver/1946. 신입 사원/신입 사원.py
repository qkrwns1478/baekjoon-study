import sys
input = sys.stdin.readline
from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list()
    for _ in range(n):
        a, b = map(int, input().split())
        heappush(arr, (a, b))

    answer = 1
    a, b = heappop(arr)
    while len(arr):
        c, d = heappop(arr)
        if d < b:
            answer += 1
            a, b = c, d
    print(answer)