from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque()
queue.append((0, 0, 0))

visited = [[False] * n for _ in range(m)]
visited[0][0] = True
answer = float("inf")

while queue:
    x, y, cnt = queue.popleft()
    if x == m-1 and y == n-1:
        answer = min(answer, cnt)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= m-1 and 0 <= ny <= n-1 and not visited[nx][ny]:
                visited[nx][ny] = True
                if arr[nx][ny] == 0 :
                    queue.appendleft((nx, ny, cnt))
                if arr[nx][ny] == 1:
                    queue.append((nx, ny, cnt+1))
                    
print(answer)