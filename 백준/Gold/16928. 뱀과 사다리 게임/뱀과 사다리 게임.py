import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
adj = dict()
for _ in range(n+m):
    a, b = map(int, input().split())
    adj[a] = b
visited = [False] * 101
queue = deque()
queue.append((1, 0))
while queue:
    now, cnt = queue.popleft()
    if now == 100:
        break
    visited[now] = True
    for i in range(1, 7):
        if 1 <= now+i <= 100:
            if now+i in adj:
                queue.append((adj[now+i], cnt+1))
            elif not visited[now+i]:
                queue.append((now+i, cnt+1))

print(cnt)