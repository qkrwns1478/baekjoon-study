N, M = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

def check(a, b, flag=True):
    if flag:
        return 0 <= a < N and 0 <= b < M and arr[a][b] == 0
    else:
        return 0 <= a < N and 0 <= b < M and arr[a][b] != 1

while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if arr[x][y] == 0:
        arr[x][y] = 2
        cnt += 1

    is_clean = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if check(nx, ny):
            is_clean = False
            break

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    if is_clean:
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 처음으로 돌아간다.
        nd = (d+2) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        if check(nx, ny, False):
            x, y = nx, ny
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else:
            break
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    else:
        # 반시계 방향으로 90° 회전한다.
        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        # 처음으로 돌아간다.
        for i in range(1, 5):
            nd = (d-i) % 4
            nx, ny = x + dx[nd], y + dy[nd]
            if check(nx, ny):
                x, y, d = nx, ny, nd
                break

print(cnt)