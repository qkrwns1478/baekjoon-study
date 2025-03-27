import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    if n == 1:
        print(1)
    else:
        dq = deque()
        for i in range(n):
            dq.append((i,arr[i])) # (인덱스, 우선순위)
            
        #print(*dq)
        arr.sort()

        key = dq[m]
        #print("key =", key)

        cnt = 0
        while dq:
            if dq[0][1] < arr[-1]:
                dq.rotate(-1)
            else:
                cnt += 1
                if key == dq.popleft():
                    print(cnt)
                    break
                else:
                    arr.pop()