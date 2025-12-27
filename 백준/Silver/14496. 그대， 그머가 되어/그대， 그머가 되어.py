from collections import deque

a, b = map(int, input().split())
N, M = map(int, input().split())
A = [set() for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    A[i].add(j)
    A[j].add(i)

queue = deque()
queue.append((a, 0))
visited = set()
visited.add(a)

res = -1
while queue:
    cur, cnt = queue.popleft()
    if cur == b:
        res = cnt
        break
    for nxt in A[cur]:
        if nxt not in visited:
            queue.append((nxt, cnt+1))
            visited.add(nxt)

print(res)
