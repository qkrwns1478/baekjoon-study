dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
AC = [0, 1]
for i in range(R):
    if arr[i][0] == -1:
        AC = [i, i+1]
        break

def circulate(AC):
    # 상단부 반시계 방향 순환
    X = AC[0]
    tmp = 0
    for j in range(1, C):
        tmp, arr[X][j] = arr[X][j], tmp
    for i in range(X-1, -1, -1):
        tmp, arr[i][C-1] = arr[i][C-1], tmp
    for j in range(C-2, -1, -1):
        tmp, arr[0][j] = arr[0][j], tmp
    for i in range(1, X):
        tmp, arr[i][0] = arr[i][0], tmp
    # 하단부 시계 방향 순환
    X = AC[1]
    tmp = 0
    for j in range(1, C):
        tmp, arr[X][j] = arr[X][j], tmp
    for i in range(X+1, R):
        tmp, arr[i][C-1] = arr[i][C-1], tmp
    for j in range(C-2, -1, -1):
        tmp, arr[R-1][j] = arr[R-1][j], tmp
    for i in range(R-2, X, -1):
        tmp, arr[i][0] = arr[i][0], tmp

def diffusion():
    tmp = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if arr[x][y] == -1:
                continue
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
                    cnt += 1
                    tmp[nx][ny] += arr[x][y] // 5
            arr[x][y] -= (arr[x][y] // 5) * cnt
    for i in range(R):
        for j in range(C):
            arr[i][j] += tmp[i][j]

for t in range(T):
    diffusion()
    # for i in range(R):
    #     print(*arr[i])
    # print("---")
    circulate(AC)
    # for i in range(R):
    #     print(*arr[i])
    # print("===")

answer = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] != -1:
            answer += arr[i][j]
print(answer)
