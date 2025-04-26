import sys
input = sys.stdin.readline
from collections import deque
dq = deque()
n = int(input())
for _ in range(n):
    q = input().split()
    if q[0] == "push_front": dq.appendleft(q[1])
    elif q[0] == "push_back": dq.append(q[1])
    elif q[0] == "pop_front":
        if dq: print(dq.popleft())
        else: print(-1)
    elif q[0] == "pop_back":
        if dq: print(dq.pop())
        else: print(-1)
    elif q[0] == "size": print(len(dq))
    elif q[0] == "empty": print(int(not dq))
    elif q[0] == "front":
        if dq: print(dq[0])
        else: print(-1)
    elif q[0] == "back":
        if dq: print(dq[-1])
        else: print(-1)