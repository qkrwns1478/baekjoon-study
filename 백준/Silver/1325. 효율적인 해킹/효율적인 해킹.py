import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
answer = [0] * (n+1)

def bfs(v):
    visited = [False] * (n+1)
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        now = queue.popleft()
        for i in adj[now]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                queue.append(i)

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)

for i in range(1, n+1):
    bfs(i)

max_val = max(answer)
result = set()

for i in range(1, n+1):
    if answer[i] == max_val:
        result.add(i)

print(*result)