import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root
        return True
    return False

v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = [i for i in range(v+1)]

answer = 0
for c, a, b in edges:
    if union(a, b):
        answer += c

print(answer)