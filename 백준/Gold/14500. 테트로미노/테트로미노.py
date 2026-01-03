N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

teto = [
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1)],
    [(1, 0), (1, 1), (2, 1)],
    [(0, -1), (1, -1), (1, -2)],
    [(1, 0), (1, -1), (2, -1)],
    [(0, 1), (1, 1), (1, 2)],
    [(1, 0), (2, 0), (2, 1)],
    [(0, 1), (0, 2), (1, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 1), (0, 2), (-1, 2)],
    [(1, 0), (2, 0), (2, -1)],
    [(0, 1), (0, 2), (1, 2)],
    [(1, 0), (2, 0), (0, 1)],
    [(1, 0), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (1, -1)],
    [(1, 0), (1, 1), (2, 0)],
    [(0, -1), (1, 0), (0, 1)],
    [(0, 1), (-1, 1), (1, 1)]
]

def get_sum(x, y, t):
    res = A[x][y]
    for i in range(3):
        nx = x + teto[t][i][0]
        ny = y + teto[t][i][1]
        if not (0 <= nx < N and 0 <= ny < M):
            return -1
        res += A[nx][ny]
    return res

answer = 0
for i in range(N):
    for j in range(M):
        for t in range(len(teto)):
            cur = get_sum(i, j, t)
            answer = max(cur, answer)
print(answer)
