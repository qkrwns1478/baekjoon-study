from copy import deepcopy

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def turn(n):
    return 1 if n == 8 else n + 1

arr = list()
for _ in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    arr.append([[a1, b1], [a2, b2], [a3, b3], [a4, b4]])

fish = dict()
for i in range(4):
    for j in range(4):
        fish[arr[i][j][0]] = (i, j, arr[i][j][1])

answer = 0
def dfs(x, y, cur, arr, fish):
    global answer

    # for i in range(4):
    #     for j in range(4):
    #         a = arr[i][j][0]
    #         if i == x and j == y:
    #             a = '상'
    #         elif a == 0:
    #             a = '_'
    #         b = arr[i][j][1]
    #         if a == '_':
    #             b = '_'
    #         else:
    #             D = ['', '↑', '↖', '←', '↙', '↓', '↘', '→', '↗']
    #             b = D[b]
    #         print(f"{a}{b} ", end='')
    #     print()
    # print()

    # 상어가 물고기 먹음
    cur += arr[x][y][0]
    del fish[arr[x][y][0]]
    arr[x][y][0] = 0

    # 물고기 이동
    for i in range(1, 17):
        if i not in fish:
            continue
        fx, fy, fd = fish[i]
        for _ in range(8):
            nfx, nfy = fx + dx[fd], fy + dy[fd]
            if 0 <= nfx < 4 and 0 <= nfy < 4 and not (nfx == x and nfy == y):
                arr[fx][fy], arr[nfx][nfy] = arr[nfx][nfy], arr[fx][fy]
                arr[nfx][nfy][1] = fd
                fish[i] = (nfx, nfy, fd)
                if arr[fx][fy][0] > 0:
                    fish[arr[fx][fy][0]] = (fx, fy, arr[fx][fy][1])
                break
            else:
                fd = turn(fd)

    # 상어 이동
    nx, ny, d = x, y, arr[x][y][1]
    flag = False
    while True:
        nx += dx[d]
        ny += dy[d]
        if not (0 <= nx < 4 and 0 <= ny < 4):
            break
        if arr[nx][ny][0] > 0:
            flag = True
            dfs(nx, ny, cur, deepcopy(arr), deepcopy(fish))

    # 상어 집으로 돌아감
    if not flag:
        answer = max(answer, cur)

dfs(0, 0, 0, arr, fish)
print(answer)
