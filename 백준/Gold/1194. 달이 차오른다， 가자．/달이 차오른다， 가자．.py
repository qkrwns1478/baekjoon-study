from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

def get_start_location():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '0':
                return (i, j)

ans = -1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
sx, sy = get_start_location()

queue = deque()
visited = set()
queue.append((sx, sy, 0, 0))
visited.add((sx, sy, 0))

def get_keys(c):
    key_map = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}
    return key_map[c.upper()]

while queue:
    x, y, cnt, keys = queue.popleft()
    if arr[x][y] == '1':
        ans = cnt
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and (nx, ny, keys) not in visited:
            if arr[nx][ny] == '#':
                continue
            elif arr[nx][ny] in {'a', 'b', 'c', 'd', 'e', 'f'}:
                nk = keys | (1 << get_keys(arr[nx][ny]))
                queue.append((nx, ny, cnt+1, nk))
                visited.add((nx, ny, nk))
            elif arr[nx][ny] in {'A', 'B', 'C', 'D', 'E', 'F'} and keys & (1 << get_keys(arr[nx][ny])) != (1 << get_keys(arr[nx][ny])):
                continue
            else:
                queue.append((nx, ny, cnt+1, keys))
                visited.add((nx, ny, keys))

print(ans)