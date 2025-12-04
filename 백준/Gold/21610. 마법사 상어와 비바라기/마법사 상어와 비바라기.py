N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for mm in range(M):
    d, s = map(int, input().split())
    prev = set()
    # 구름 이동
    while clouds:
        x, y = clouds.pop()
        nx, ny = x + dx[d] * s, y + dy[d] * s
        while nx < 0: nx += N
        while nx >= N: nx -= N
        while ny < 0: ny += N
        while ny >= N: ny -= N
        A[nx][ny] += 1
        prev.add((nx, ny))
    # 물복사버그
    for x, y in prev:
        cnt = 0
        for i in range(2, 9, 2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                cnt += 1
        A[x][y] += cnt
    # 새로운 구름 생성
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and (i, j) not in prev:
                clouds.append((i, j))
                A[i][j] -= 2

answer = 0
for i in range(N):
    for j in range(N):
        answer += A[i][j]
print(answer)