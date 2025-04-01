import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
D = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b) # a의 키 < b의 키
    D[b] += 1
    
queue = deque()
for i in range(1, n+1):
    if D[i] == 0:
        queue.append(i)

result = list()
while queue:
    now = queue.popleft()
    result.append(now)
    for i in adj[now]:
        D[i] -= 1
        if D[i] == 0:
            queue.append(i)

print(*result)