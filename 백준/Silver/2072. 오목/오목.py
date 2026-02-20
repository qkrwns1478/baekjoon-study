board = [[0] * 19 for _ in range(19)]
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def check(x, y):
    p = board[x][y]
    if p == 0:
        return 0
    for i in range(4):
        cnt = 1
        # 정방향
        nx, ny = x + dx[i], y + dy[i]
        while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == p:
            cnt += 1
            nx += dx[i]
            ny += dy[i]
        # 역방향
        rx, ry = x - dx[i], y - dy[i]
        while 0 <= rx < 19 and 0 <= ry < 19 and board[rx][ry] == p:
            cnt += 1
            rx -= dx[i]
            ry -= dy[i]
        if cnt == 5:
            # 6목 방지
            if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == p:
                continue
            if 0 <= rx < 19 and 0 <= ry < 19 and board[rx][ry] == p:
                continue
            return True
    return False

cnt = 0
player = 1

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y] = player
    cnt += 1

    if check(x, y):
        print(cnt)
        exit()
    player = 3 - player

print(-1)
