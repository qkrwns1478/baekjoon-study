import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

def dfs(now, d):
    global flag
    if d == 5 or flag:
        flag = True
        return
    
    visited[now] = True
    for i in arr[now]:
        if not visited[i]:
            dfs(i, d+1)
    visited[now] = False

flag = False
for i in range(n):
    dfs(i, 1)
    if flag:
        break

print(1 if flag else 0)