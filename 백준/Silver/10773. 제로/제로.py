import sys
from collections import deque

k = int(sys.stdin.readline())
stack = deque()

for _ in range(k):
    n = int(sys.stdin.readline())
    if n > 0:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))