N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

#    [←, ↓, →, ↑]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
#     [↙, ↘, ↗, ↖]
ddx = [1, 1, -1, -1]
ddy = [-1, 1, 1, -1]

fall = 0

def move_sand(x, y, m):
    if 0 <= x < N and 0 <= y < N:
        A[x][y] += m
    else:
        global fall
        fall += m

def storm(d, x, y): # (x, y)는 그림에서 'y'로 표시된 부분
    cur = A[x][y]
    A[x][y] = 0
    # 대각선 방향 처리
    diag_ten = [[3, 0], [0, 1], [1, 2], [2, 3]]
    for i in range(4):
        if i in diag_ten[d]:
            move_sand(x + ddx[i], y + ddy[i], cur // 10)
        else:
            move_sand(x + ddx[i], y + ddy[i], cur // 100)
    # 3방향 처리
    d_down = (d + 1) % 4
    d_up = (d - 1) % 4
    move_sand(x + dx[d_down], y + dy[d_down], (cur * 7) // 100)
    move_sand(x + 2 * dx[d_down], y + 2 * dy[d_down], (cur * 2) // 100)
    move_sand(x + dx[d_up], y + dy[d_up], (cur * 7) // 100)
    move_sand(x + 2 * dx[d_up], y + 2 * dy[d_up], (cur * 2) // 100)
    move_sand(x + 2 * dx[d], y + 2 * dy[d], (cur * 5) // 100)
    # a 처리
    rem = cur - (cur // 10 + cur // 10 + cur // 100 + cur // 100 + (cur * 7) // 100 + (cur * 7) // 100 + (cur * 2) // 100 + (cur * 2) // 100 + (cur * 5) // 100)
    move_sand(x + dx[d], y + dy[d], rem)

x, y = N // 2, N // 2
for i in range(1, N):
    if i % 2 == 1:
        for _ in range(i):
            y -= 1
            storm(0, x, y)
        for _ in range(i):
            x += 1
            storm(1, x, y)
    else:
        for _ in range(i):
            y += 1
            storm(2, x, y)
        for _ in range(i):
            x -= 1
            storm(3, x, y)
for _ in range(N-1):
    y -= 1
    storm(0, x, y)
print(fall)
