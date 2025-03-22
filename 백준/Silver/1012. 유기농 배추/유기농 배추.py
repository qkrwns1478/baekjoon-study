import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def baechu(x, y):
    if visited[x][y]:
        return
    
    visited[x][y] = True
    
    if arr[x][y] > 0:
        if x > 0 and not visited[x-1][y]:
            baechu(x-1, y)
        if x < n-1 and not visited[x+1][y]:
            baechu(x+1, y)
        if y < m-1 and not visited[x][y+1]:
            baechu(x, y+1)
        if y > 0 and not visited[x][y-1]:
            baechu(x, y-1)
            
    return

t = int(input())
for _ in range(t):
    n, m ,k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int,input().split())
        arr[x][y] = 1

    #for i in range(n):
    #    print(*arr[i])
    #print()

    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] > 0:
                baechu(i, j)
                cnt += 1
    print(cnt)