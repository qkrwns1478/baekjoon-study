import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y, size, n, arr):
    queue = deque([(x, y, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    fish = list()

    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if arr[nx][ny] <= size and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
                    if 0 < arr[nx][ny] < size:
                        fish.append((dist + 1, nx, ny))
    
    if fish:
        fish.sort()
        return fish[0]
    else:
        return None

n = int(input())
arr = list()
posX, posY = 0, 0
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(n):
        if row[j] == 9:
            posX, posY = i, j
            arr[i][j] = 0

size = 2
count = 0
time = 0

while True:
    target = bfs(posX, posY, size, n, arr)
    if target is None:
        break
    dist, fishX, fishY = target
    time += dist
    count += 1
    if count == size:
        size += 1
        count = 0
    arr[fishX][fishY] = 0
    posX, posY = fishX, fishY
    
print(time)