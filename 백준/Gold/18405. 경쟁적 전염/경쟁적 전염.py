import sys
input = sys.stdin.readline
#from heapq import heappush, heappop
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, X, Y = map(int, input().split())
# s초 뒤에 (x,y)에 존재하는 바이러스 출력
# 번호가 낮은 바이러스부터 먼저 증식

queue = list()
for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            #heappush(queue, (arr[i][j], i, j, 0))
            queue.append((arr[i][j], i, j, 0))
queue.sort()
queue = deque(queue)

while queue:
    #num, x, y, time = heappop(queue)
    num, x, y, time = queue.popleft()
    if time == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= n-1:
            if arr[nx][ny] == 0:
                arr[nx][ny] = num
                #heappush(queue, (arr[nx][ny], nx, ny, time+1))
                queue.append((arr[nx][ny], nx, ny, time+1))

print(arr[X-1][Y-1])