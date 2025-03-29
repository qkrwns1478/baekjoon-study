import sys
input = sys.stdin.readline
import heapq

m, n, h = map(int, input().split())
arr = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

tomatoes = list()
for i in range(h):
    for j in range(n):
        arr[i][j] = list(map(int, input().split()))
        for k in range(m):
            if arr[i][j][k] == 1:
                tomatoes.append((i, j, k)) # (z, x, y)

visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

def dij():
    dz = [0, 0, 0, 0, 1, -1]
    dx = [0, 1, 0, -1, 0, 0]
    dy = [1, 0, -1, 0, 0, 0]

    queue = list()
    for tz, tx, ty in tomatoes:
        heapq.heappush(queue, (0, tz, tx, ty))

    while queue:
        day, z, x, y = heapq.heappop(queue)

        if visited[z][x][y]:
            continue

        visited[z][x][y] = True

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz <= h-1 and 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if arr[nz][nx][ny] == 0 and not visited[nz][nx][ny]:
                    arr[nz][nx][ny] = 1
                    heapq.heappush(queue, (day+1, nz, nx, ny))

    return day

if tomatoes:
    answer = dij()

    flag = True
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 0:
                    flag = False
                    break
            
    if flag:
        print(answer)
    else:
        print(-1)

else:
    print(-1)