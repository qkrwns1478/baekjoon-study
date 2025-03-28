import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations as comb

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

n = int(input())
stars = []

for i in range(n):
    x, y = map(float, input().split())
    stars.append((i, x, y))

edges = []
cmb = comb(stars, 2)

for c in cmb:
    cost_x = abs(c[0][1] - c[1][1])
    cost_y = abs(c[0][2] - c[1][2])
    cost = (cost_x ** 2 + cost_y ** 2) ** 0.5
    edges.append((cost, c[0][0], c[1][0]))
del cmb
del stars

edges.sort()

parent = [i for i in range(n+1)]
answer = 0
    
for c, a, b in edges:
    if union(a, b):
        answer += c

print("%.2f" % answer)