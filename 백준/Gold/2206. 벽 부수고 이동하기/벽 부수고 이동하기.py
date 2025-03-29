import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

def bfs(x, y):
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    # visited[][][0] : 벽 안 부쉈을 때
    # visited[][][1] : 벽 부쉈을 때
    queue = deque()
    queue.append((x, y, 0))
    visited[0][0][0] = 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        x, y, b = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][b]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 다음 칸이 빈 칸
                if arr[nx][ny] == 0 and visited[nx][ny][b] == 0:
                    visited[nx][ny][b] = visited[x][y][b] + 1
                    queue.append((nx, ny, b))
                    
                # 다음 칸이 벽이고 아직 안 부쉈을 떄
                if arr[nx][ny] == 1 and b == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][b] + 1
                    queue.append((nx, ny, 1))

    return -1

print(bfs(0, 0))