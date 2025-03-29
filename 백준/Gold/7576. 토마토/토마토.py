import sys
input = sys.stdin.readline
import heapq

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tomatoes = list()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            tomatoes.append((i, j))

visited = [[False for _ in range(m)] for _ in range(n)]

def dij():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    queue = list()
    for tx, ty in tomatoes:
        heapq.heappush(queue, (0, tx, ty))

    while queue:
        day, x, y = heapq.heappop(queue)

        if visited[x][y]:
            continue

        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if arr[nx][ny] == 0 and not visited[nx][ny]:
                    arr[nx][ny] = 1
                    heapq.heappush(queue, (day+1, nx, ny))

    return day

if tomatoes:
    answer = dij()

    flag = True
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                flag = False
                break
            
    if flag:
        print(answer)
    else:
        print(-1)

else:
    print(-1)