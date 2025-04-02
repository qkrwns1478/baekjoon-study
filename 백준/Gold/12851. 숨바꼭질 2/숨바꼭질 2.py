import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
queue = deque()
queue.append((n, 0))
result = list()

while queue:
    now, time = queue.popleft()
    visited[now] = True
    
    if now == k:
        result.append(time)
        
    for next in [now-1, now+1, 2*now]:
        if 0 <= next <= 100000 and not visited[next]:
            queue.append((next, time+1))

min_val = min(result)
print(min_val)
print(result.count(min_val))