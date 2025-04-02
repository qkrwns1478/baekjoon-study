import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

n, m = map(int, input().split())
H = [[] for _ in range(n+1)]
L = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    if b not in H[a]:
        H[a].append(b)
    if a not in L[b]:
        L[b].append(a)

answer = 0
mid = (n+1)//2

def dfs(arr, i):
    cnt = 0
    for j in arr[i]:
        if not visited[j]:
            visited[j] = True
            cnt += 1
            cnt += dfs(arr, j)    
    return cnt

for i in range(1, n+1):
    visited = [False] * (n+1)
    if dfs(H, i) >= mid:
        answer += 1
    if dfs(L, i) >= mid:
        answer += 1

print(answer)