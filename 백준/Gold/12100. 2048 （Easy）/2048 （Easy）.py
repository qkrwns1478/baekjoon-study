from copy import deepcopy

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def get_max_val(arr):
    res = 0
    for i in range(N):
        for j in range(N):
            res = max(res, arr[i][j])
    return res

def game(level, arr, d):
    # d 방향으로 블록들 이동
    if d == 1:
        range_i = range(N)
        range_j = range(N-1, -1, -1)
    elif d == 2:
        range_i = range(N-1, -1, -1)
        range_j = range(N)
    else:
        range_i = range(N)
        range_j = range(N)

    merged = set()
    for i in range_i:
        for j in range_j:
            if arr[i][j] == 0:
                continue
            ci, cj = i, j
            while True:
                ni, nj = ci + dx[d], cj + dy[d]
                if not (0 <= ni < N and 0 <= nj < N):
                    break
                elif arr[ni][nj] == 0:
                    arr[ni][nj] = arr[ci][cj]
                    arr[ci][cj] = 0
                    ci, cj = ni, nj
                elif arr[ci][cj] == arr[ni][nj] and (ni, nj) not in merged:
                    arr[ni][nj] *= 2
                    arr[ci][cj] = 0
                    merged.add((ni, nj))
                    break
                else:
                    break

    # 5번째 이동이면 종료
    if level == 5:
        global answer
        answer = max(answer, get_max_val(arr))
        return

    # 다음 방향 결정
    for nd in range(4):
        game(level+1, deepcopy(arr), nd)

for d in range(4):
    game(1, deepcopy(arr), d)

print(answer)
