from heapq import *

T = int(input())
for _ in range(T):
    K = int(input())
    C = list(map(int, input().split()))
    heapify(C)
    ans = 0
    while len(C) > 1:
        tmp = 0
        a = heappop(C)
        b = heappop(C)
        tmp += a + b
        ans += tmp
        heappush(C, tmp)
    print(ans)
