import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = list()
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    
D = [float("inf")] * (n+1)
D[1] = 0

for _ in range(n-1):
    for s, e, w in edges:
        if D[s] != float("inf") and D[e] > D[s] + w:
            D[e] = D[s] + w

flag = False
for s, e, w in edges:
    if D[s] != float("inf") and D[e] > D[s] + w:
        flag = True
        break

if flag: print(-1)
else:
    for i in range(2, n+1):
        print(D[i] if D[i] != float("inf") else -1)