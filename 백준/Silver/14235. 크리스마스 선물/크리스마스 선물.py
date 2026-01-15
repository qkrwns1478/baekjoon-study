from heapq import heappush, heappop

n = int(input())
queue = list()
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if not queue:
            print(-1)
        else:
            print(-heappop(queue))
    else:
        for i in range(a[0]):
            heappush(queue, -a[1+i])
