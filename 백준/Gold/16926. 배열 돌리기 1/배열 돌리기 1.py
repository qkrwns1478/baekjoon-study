from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [[0] * M for _ in range(N)]
visited = set()

lmt = N // 2 if N <= M and N % 2 == 0 else M // 2
for i in range(lmt):
    tmp = [(i, i)]
    visited.add((i, i))
    cur_d = 0
    while True:
        if cur_d != 0 and tmp[-1] == (i, i):
            break
        elif tmp[-1][0] + dx[cur_d] == i and tmp[-1][1] + dy[cur_d] == i:
            break
        for d in range(cur_d, 4):
            nx, ny = tmp[-1][0] + dx[d], tmp[-1][1] + dy[d]
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                tmp.append((nx, ny))
                visited.add((nx, ny))
                break
        cur_d = d
    # print(tmp)
    dq = deque(tmp)
    dq.rotate(-R)
    for j in range(len(tmp)):
        B[dq[j][0]][dq[j][1]] = A[tmp[j][0]][tmp[j][1]]

for i in range(N):
    print(*B[i])
