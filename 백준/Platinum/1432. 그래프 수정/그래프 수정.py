import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
adj = [[] for _ in range(n+1)]
D = [0] * (n+1)

for i in range(1, n+1):
    s = input()
    for j in range(n):
        if s[j] == "1":
            #adj[i].append(j+1)
            adj[j+1].append(i)
            #D[j+1] += 1
            D[i] += 1

queue = list()
for i in range(1, n+1):
    #adj[i].sort()
    if D[i] == 0:
        heappush(queue, -i)

result = [0] * (n+1)
idx = n
while queue:
    now = -heappop(queue)
    result[now] = idx
    idx -= 1
    for i in adj[now]:
        D[i] -= 1
        if D[i] == 0:
            heappush(queue, -i)
    #print(queue)
    #print(result)

flag = True
for i in range(1, n+1):
    if result[i] == 0:
        flag = False
        break
    
print(*result[1:]) if flag else print(-1)