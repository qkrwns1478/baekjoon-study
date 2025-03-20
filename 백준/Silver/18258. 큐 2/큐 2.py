import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()
for _ in range(n):
    query = sys.stdin.readline().split()

    if query[0] == "push":
        dq.append(query[1])

    elif query[0] == "pop":
        print(dq.popleft() if dq else -1)

    elif query[0] == "size":
        print(len(dq))

    elif query[0] == "empty":
        print(0 if dq else 1)

    elif query[0] == "front":
        print(dq[0] if dq else -1)

    elif query[0] == "back":
        print(dq[-1] if dq else -1)