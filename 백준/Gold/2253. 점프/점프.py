import sys
input = sys.stdin.readline
from collections import deque

dv = [1, 0, -1]
n, m = map(int, input().split())
arr = set(int(input()) for _ in range(m))
visited = dict()
visited[1] = set()
visited[1].add(0)

queue = deque()
queue.append((1, 0, 0))
answer = float("inf")

while queue:
    s, v, cnt = queue.popleft()
    #visited[s].add(v)
    if s == n:
        answer = cnt
        break
    for i in range(3):
        nv = v + dv[i]
        ns = s + nv
        if nv >= 1 and 1 <= ns <= n and ns not in arr:
            if ns not in visited:
                visited[ns] = set()
            if nv not in visited[ns]:
                visited[ns].add(nv)
                queue.append((ns, nv, cnt+1))

print(answer if answer < float("inf") else -1)