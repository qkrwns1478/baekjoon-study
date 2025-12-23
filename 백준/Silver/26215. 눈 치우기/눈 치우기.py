from heapq import heappush, heappop

N = int(input())
A = list(map(int, input().split()))
hq = list()

for i in range(N):
    heappush(hq, -A[i])

time = 0
while hq:
    if len(hq) >= 2:
        a = heappop(hq)
        b = heappop(hq)
        a += 1
        b += 1
        if a != 0:
            heappush(hq, a)
        if b != 0:
            heappush(hq, b)
    else:
        a = heappop(hq)
        a += 1
        if a != 0:
            heappush(hq, a)
    time += 1

print(time if time <= 1440 else -1)
