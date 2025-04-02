import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= h-1 and 0 <= ny <= w-1:
            if not visited[nx][ny] and arr[nx][ny] == 1:
                dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    arr = [[] for _ in range(h)]
    for i in range(h):
        arr[i] = list(map(int, input().split()))
    visited = [[False] * w for _ in range(h)]

    answer = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j] == 1:
                dfs(i, j)
                answer += 1
    print(answer)