from collections import deque
from bisect import bisect_left, bisect_right

n, T = map(int, input().split())
arr = list()
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((y, x))
arr.sort()

INF = float("inf")
ans = -1

queue = deque()
queue.append((0, 0, 0))
visited = set()
visited.add((0, 0))

while queue:
    y, x, cnt = queue.popleft()
    if y == T:
        ans = cnt
        break
    l = bisect_left(arr, (y-2, -INF))
    r = bisect_right(arr, (y+2, INF))
    for i in range(l, r):
        b, a = arr[i]
        if (a, b) in visited:
            continue
        if abs(a-x) <= 2 and abs(b-y) <= 2:
            visited.add((a, b))
            queue.append((b, a, cnt+1))

print(ans)