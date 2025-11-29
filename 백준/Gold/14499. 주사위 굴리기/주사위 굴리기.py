N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [0] * 7
top, east, north = 1, 3, 2

def op(n):
    return 7 - n

def is_valid(x, y, k):
    nx = x + dx[k]
    ny = y + dy[k]
    return 0 <= nx < N and 0 <= ny < M

def roll(direction):
    global top, east, north
    if direction == 1: # 동쪽
        nt, ne, nn = op(east), top, north
    elif direction == 2: # 서쪽
        nt, ne, nn = east, op(top), north
    elif direction == 3: # 북쪽
        nt, ne, nn = op(north), east, top
    else: # 남쪽
        nt, ne, nn = north, east, op(top)
    return nt, ne, nn

for k in cmd:
    if not is_valid(x, y, k):
        continue
    x += dx[k]
    y += dy[k]
    top, east, north = roll(k)
    if arr[x][y] == 0:
        arr[x][y] = dice[op(top)]
    else:
        dice[op(top)] = arr[x][y]
        arr[x][y] = 0
    print(dice[top])