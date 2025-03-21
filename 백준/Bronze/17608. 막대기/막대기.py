import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()
for _ in range(n):
    k = int(sys.stdin.readline())
    while dq and dq[-1] <= k:
        dq.pop()
    dq.append(k)
    #print(*dq)
print(len(dq))