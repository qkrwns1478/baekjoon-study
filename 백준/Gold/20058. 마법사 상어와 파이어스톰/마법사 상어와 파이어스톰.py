N, Q = map(int, input().split())
grid_size = 2 ** N
A = [list(map(int, input().split())) for _ in range(grid_size)]
L = list(map(int, input().split()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def rotate(l):
    if l == 0:
        return
    global A
    tmp = [row[:] for row in A]
    sub_size = 2 ** l
    for y in range(0, grid_size, sub_size):
        for x in range(0, grid_size, sub_size):
            for i in range(sub_size):
                for j in range(sub_size):
                    tmp[y + j][x + sub_size - 1 - i] = A[y + i][x + j]
    A = tmp

def melt():
    candidates = list()
    for x in range(grid_size):
        for y in range(grid_size):
            if A[x][y] == 0:
                continue
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < grid_size and 0 <= ny < grid_size:
                    if A[nx][ny] > 0:
                        cnt += 1
            if cnt < 3:
                candidates.append((x, y))
    for x, y in candidates:
        if A[x][y] > 0:
            A[x][y] -= 1

for l in L:
    rotate(l)
    melt()

def dfs(x, y):
    global visited
    stack = [(x, y)]
    cnt = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited and A[nx][ny] > 0:
                visited.add((nx, ny))
                stack.append((nx, ny))
                cnt += 1
    return cnt

total = sum(sum(row) for row in A)
max_ice = 0
visited = set()
for i in range(grid_size):
    for j in range(grid_size):
        if A[i][j] > 0 and (i, j) not in visited:
            visited.add((i, j))
            max_ice = max(max_ice, dfs(i, j))
print(total)
print(max_ice)
