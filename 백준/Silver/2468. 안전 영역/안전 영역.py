import sys
sys.setrecursionlimit(10**6)

def find_safe(h, x, y):
    if visited[x][y]:
        return
    
    visited[x][y] = True
    
    if arr[x][y] > h:
        if x > 0 and not visited[x-1][y]:
            find_safe(h, x-1, y)
        if x < n-1 and not visited[x+1][y]:
            find_safe(h, x+1, y)
        if y < n-1 and not visited[x][y+1]:
            find_safe(h, x, y+1)
        if y > 0 and not visited[x][y-1]:
            find_safe(h, x, y-1)
            
    return

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
max_h = 0
for i in range(n):
    arr[i] = list(map(int, input().split()))
    max_h = max(max_h, max(arr[i]))

max_safe = 0
for i in range(max_h):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if not visited[j][k] and arr[j][k] > i:
                find_safe(i, j, k)
                cnt += 1
    max_safe = max(max_safe, cnt)

print(max_safe)