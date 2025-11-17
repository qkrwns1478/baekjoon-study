import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
graph[0].append(R)

parent = [-1] * (N+1)
child = [[] for _ in range(N+1)]
stack = list()
stack.append(0)

while stack:
    cur = stack.pop()
    for ch in graph[cur]:
        if parent[ch] != -1:
            continue
        child[cur].append(ch)
        parent[ch] = cur
        stack.append(ch)

size = [0] * (N+1)
def count_nodes(cur):
    size[cur] = 1
    for ch in child[cur]:
        count_nodes(ch)
        size[cur] += size[ch]

count_nodes(R)

for _ in range(Q):
    print(size[int(input())])