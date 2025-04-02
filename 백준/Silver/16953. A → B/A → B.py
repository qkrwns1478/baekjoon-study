import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
queue = deque()
visited = set()
queue.append((a,0))
flag = False
while queue:
    now, cnt = queue.popleft()
    if now == b:
        flag = True
        break
    elif now > b:
        break
    visited.add(now)
    for i in (10*now + 1, 2*now):
        if i not in visited and i <= b:
            queue.append((i, cnt+1))
print(cnt+1 if flag else -1)