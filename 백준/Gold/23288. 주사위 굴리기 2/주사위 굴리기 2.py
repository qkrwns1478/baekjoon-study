from collections import deque

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
X, Y = 1, 1
D = 0
top, east, north = 1, 3, 2
score = 0

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def get_opposite_direction(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    else:
        return 1

def get_score(x, y):
    b = A[x-1][y-1]
    c = 0
    queue = deque()
    queue.append((x-1, y-1))
    visited = set()
    visited.add((x-1, y-1))
    while queue:
        c += 1
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if (nx, ny) not in visited and A[nx][ny] == b:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return b * c

def op(n):
    return 7 - n

def roll(d):
    global top, east, north
    if d == 0:  # 동쪽
        nt, ne, nn = op(east), top, north
    elif d == 1:  # 남쪽
        nt, ne, nn = north, east, op(top)
    elif d == 2:  # 서쪽
        nt, ne, nn = east, op(top), north
    else:  # 북쪽
        nt, ne, nn = op(north), east, top
    return nt, ne, nn

for k in range(K):
    nx, ny = X + dx[D], Y + dy[D]
    if not (1 <= nx <= N and 1 <= ny <= M):
        D = get_opposite_direction(D)
        nx, ny = X + dx[D], Y + dy[D]
    X, Y = nx, ny
    top, east, north = roll(D)
    score += get_score(X, Y)
    a = op(top)
    b = A[X-1][Y-1]
    if a > b:
        D = (D + 1) % 4
    elif a < b:
        D = (D - 1) % 4
    # print(f"#{k+1} ({X}, {Y}) {get_score(X, Y)}")

print(score)
