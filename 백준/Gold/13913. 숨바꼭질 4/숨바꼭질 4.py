import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
queue = deque()
queue.append((n, 0))
log = [-1] * 100001

while queue:
    now, time = queue.popleft()
    visited[now] = True
    
    if now == k:
        print(time)
        break
    
    for node in [now-1, now+1, 2*now]:
        if 0 <= node <= 100000 and not visited[node]:
            queue.append((node, time+1))
            if log[node] == -1:
                log[node] = now

result = list()
result.append(k)
cnt = time
while cnt > 0:
    result.append(log[result[-1]])
    cnt -= 1
result.reverse()
print(*result)