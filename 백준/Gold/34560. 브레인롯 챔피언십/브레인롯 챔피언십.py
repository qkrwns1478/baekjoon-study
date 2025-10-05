from collections import deque

n = int(input())
arr = list()
G = [list() for _ in range(n)]
D = [0] * n

for i in range(n):
    name, p, a, s = input().split()
    arr.append((name, int(p), int(a), int(s)))

for i in range(1, n):
    for j in range(i):
        point_i, point_j = 0, 0
        for k in range(1, 4):
            if arr[i][k] > arr[j][k]:
                point_i += 1
            elif arr[i][k] < arr[j][k]:
                point_j += 1
            else:
                point_i += 1
                point_j += 1
        if point_i > point_j:
            D[j] += 1
            G[i].append(j)
        elif point_i < point_j:
            D[i] += 1
            G[j].append(i)

res = list()
queue = deque()
for i in range(n):
    if D[i] == 0:
        queue.append(i)
        res.append(arr[i][0])

tmp = list()
while queue:
    cur = queue.popleft()
    tmp.append(cur)
    for g in G[cur]:
        D[g] -= 1
        if D[g] == 0:
            queue.append(g)

if len(tmp) != len(arr):
    print("Paradoxe Absurdo")
elif not res:
    print("Paradoxe Absurdo")
else:
    res.sort()
    for r in res:
        print(r)