import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
dq = deque(range(1, n+1))
stack = deque()

while dq:
    try:
        stack.append(dq[k-1])
        dq.remove(dq[k-1])
        dq.rotate(-k+1)
    except:
        break 

while dq:
    if dq:
        stack.append(dq.popleft())
        dq.rotate(1-k)

print("<", end="")
print(*stack, sep=", ", end="")
print(">")