from collections import deque
import sys
input = sys.stdin.readline

l, w = map(int, input().split())
arr = [[0] * w for _ in range(l)]
for i in range(l):
    s = input().strip()
    for j in range(w):
        if s[j] == 'L':
            arr[i][j] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0

def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy, 0))
    visited = set()
    visited.add((sx, sy))
    while queue:
        x, y, t = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < w:
                if (nx, ny) not in visited and arr[nx][ny] == 1:
                    visited.add((nx, ny))
                    queue.append((nx, ny, t+1))
    return t

for i in range(l):
    for j in range(w):
        if arr[i][j] == 1:
            answer = max(answer, bfs(i, j))
print(answer)