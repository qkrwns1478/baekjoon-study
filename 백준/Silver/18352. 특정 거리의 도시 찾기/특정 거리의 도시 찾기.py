import sys
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1

    while queue:
        now = queue.popleft()
        for i in adj[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)

bfs(x)

answer = list()
for i in range(n+1):
    if visited[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)