from collections import deque
from sys import stdin
input = stdin.readline

N, M, fuel = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
X, Y = map(int, input().split())
X -= 1
Y -= 1

P, D, arrived = list(), list(), set()
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    P.append((sx-1, sy-1))
    D.append((ex-1, ey-1))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy, ex, ey):
    queue = deque()
    visited = set()
    queue.append((sx, sy, 0))
    visited.add((sx, sy))
    while queue:
        x, y, d = queue.popleft()
        if x == ex and y == ey:
            return d
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny, d+1))
                visited.add((nx, ny))
    return float('inf')

# S = [bfs(P[i][0], P[i][1], D[i][0], D[i][1]) for i in range(M)]

def get_nearest_passenger():
    global X, Y, P, arrived
    # res = list()
    # for i in range(M):
    #     if i not in arrived:
    #         res.append((bfs(X, Y, P[i][0], P[i][1]), P[i][0], P[i][1], i))
    # res.sort(key=lambda x: (x[0], x[1], x[2]))
    # return res[0][3], res[0][0]
    p_map = {P[i]: i for i in range(M) if i not in arrived}
    queue = deque()
    queue.append((X, Y, 0))
    visited = set()
    visited.add((X, Y))
    candidates = list()
    min_dist = float('inf')
    while queue:
        x, y, d = queue.popleft()
        if d > min_dist:
            break
        if (x, y) in p_map:
            min_dist = d
            candidates.append((d, x, y, p_map[(x, y)]))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny, d+1))
                visited.add((nx, ny))
    if not candidates:
        return -1, -1
    candidates.sort()
    return candidates[0][3], candidates[0][0]

while fuel > 0 and len(arrived) < M:
    nearest_p, nearest_dist = get_nearest_passenger()
    if nearest_p == -1:
        break
    drive = bfs(P[nearest_p][0], P[nearest_p][1], D[nearest_p][0], D[nearest_p][1])
    used_fuel = nearest_dist + drive
    if fuel - used_fuel < 0:
        break
    fuel = fuel - used_fuel + drive * 2
    arrived.add(nearest_p)
    X, Y = D[nearest_p]

print(fuel if len(arrived) == M else -1)
