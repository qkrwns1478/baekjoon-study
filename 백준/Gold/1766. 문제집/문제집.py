from collections import defaultdict
from heapq import heappush, heappop

n, m = map(int, input().split())
adj = defaultdict(list)
D = [0] * (n+1)
queue = list()
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    D[b] += 1
for i in range(1, n+1):
    if D[i] == 0:
        heappush(queue, i)

result = list()
while queue:
    q = heappop(queue)
    result.append(q)
    for j in adj[q]:
        D[j] -= 1
        if D[j] == 0:
            heappush(queue, j)

for i in range(1, n+1):
    if i not in result:
        result.append(i)

print(*result)