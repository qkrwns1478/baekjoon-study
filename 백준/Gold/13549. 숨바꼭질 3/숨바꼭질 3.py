import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
queue = deque()
queue.append((n, 0))

while queue:
    now, time = queue.popleft()
    visited[now] = True
    
    if now == k:
        print(time)
        break

    if 0 <= now*2 <= 100000 and not visited[now*2]:
        queue.append((now*2, time))
    if 0 <= now-1 <= 100000 and not visited[now-1]:
        queue.append((now-1, time+1))
    if 0 <= now+1 <= 100000 and not visited[now+1]:
        queue.append((now+1, time+1))