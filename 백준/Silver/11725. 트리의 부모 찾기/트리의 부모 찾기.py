import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def hello(i, p):
    if parents[i]:
        return

    parents[i] = p

    for j in range(len(adj[i])):
        hello(adj[i][j], i)
    

n = int(input())
adj = dict()

for i in range(1, n+1):
    adj[i] = list()

for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    adj[a].sort()
    adj[b].sort()

#for i in range(1, n+1):
#    print(f"{i} : {adj[i]}")

parents = [None] * (n+1)
hello(1, 1)

for i in range(2, n+1):
    print(parents[i])
