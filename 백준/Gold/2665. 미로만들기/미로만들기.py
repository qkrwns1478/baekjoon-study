import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = [list(map(int,input().strip())) for _ in range(n)]

def dij(x, y):
    visited = [[False for _ in range(n)] for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    queue = []
    heapq.heappush(queue, (0, x, y))

    while queue:
        cnt, x, y = heapq.heappop(queue)

        if visited[x][y]:
            continue

        visited[x][y] = True

        if x == n-1 and y == n-1:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    arr[nx][ny] = arr[x][y] + 1
                    heapq.heappush(queue, (cnt, nx, ny))
                elif arr[nx][ny] == 0 and not visited[nx][ny]:
                    arr[nx][ny] = arr[x][y] + 1
                    heapq.heappush(queue, (cnt+1, nx, ny))

print(dij(0, 0))