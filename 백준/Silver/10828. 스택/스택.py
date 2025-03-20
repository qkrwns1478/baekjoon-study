import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()
for _ in range(n):
    query = sys.stdin.readline().split()

    if query[0] == "push":
        stack.append(query[1])

    elif query[0] == "pop":
        print(stack.pop() if stack else -1)

    elif query[0] == "size":
        print(len(stack))

    elif query[0] == "empty":
        print(0 if stack else 1)

    elif query[0] == "top":
        print(stack[-1] if stack else -1)