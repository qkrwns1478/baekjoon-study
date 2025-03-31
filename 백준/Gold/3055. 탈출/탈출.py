import sys
import heapq

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ex, ey = 0, 0
sx, sy = 0, 0
water = list()

for i in range(r):
    for j in range(c):
        if arr[i][j] == "D":
            ex, ey = i, j
        elif arr[i][j] == "S":
            sx, sy = i, j
            arr[i][j] = "."
        elif arr[i][j] == "*":
            water.append((i, j))

visitedW = [[False] * c for _ in range(r)]
visitedS = [[False] * c for _ in range(r)]

def dochi():
    queueW = list()
    queueS = list()

    for wx, wy in water:
        heapq.heappush(queueW, (0, wx, wy))
        visitedW[wx][wy] = True

    heapq.heappush(queueS, (0, sx, sy))
    visitedS[sx][sy] = True

    while queueS:
        #print(queueW)
        #print(queueS)
        '''for i in range(r):
            print(*arr[i])
        print("-" * 20)'''
        
        while queueW and queueW[0][0] <= queueS[0][0]:
            time, x, y = heapq.heappop(queueW)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx <= r-1 and 0 <= ny <= c-1:
                    if arr[nx][ny] == "." and not visitedW[nx][ny]:
                        arr[nx][ny] = "*"
                        visitedW[nx][ny] = True
                        heapq.heappush(queueW, (time+1, nx, ny))

        time, x, y = heapq.heappop(queueS)
        #print(f"Dochi is at ({x}, {y})")
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= r-1 and 0 <= ny <= c-1:
                if nx == ex and ny == ey:
                    return time + 1
                if arr[nx][ny] == "." and not visitedS[nx][ny]:
                    visitedS[nx][ny] = True
                    heapq.heappush(queueS, (time+1, nx, ny))

    return "KAKTUS"

print(dochi())