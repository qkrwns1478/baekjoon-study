from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def is_null(arr):
    for i in range(len(arr)):
        if arr[i] != 0:
            return False
    return True

N, M, T = map(int, input().split())
circles = [deque(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y):
    global visited
    res = set()
    res.add((x, y))
    for i in range(4):
        nx, ny = x + dx[i], (y + dy[i]) % M
        if 0 <= nx < N and 0 <= ny < M:
            if (nx, ny) not in visited and circles[nx][ny] == circles[x][y]:
                visited.add((nx, ny))
                res.update(dfs(nx, ny))
    return res

# def draw():
#     for i in range(N):
#         for j in range(M):
#             print(circles[i][j] if circles[i][j] > 0 else 'X', end=' ')
#         print()

for _ in range(T):
    x, d, k = map(int, input().split())
    r = k if d == 0 else -k
    visited = set()
    adj = list()

    for i in range(N):
        if (i+1) % x == 0:
            circles[i].rotate(r)

    for i in range(N):
        if not is_null(circles[i]):
            for j in range(M):
                if circles[i][j] != 0 and (i, j) not in visited:
                    visited.add((i, j))
                    a = dfs(i, j)
                    if len(a) > 1:
                        adj.append(a)
    if adj:
        for a in adj:
            for i, j in a:
                circles[i][j] = 0
    else:
        tot, cnt = 0, 0
        for i in range(N):
            for j in range(M):
                if circles[i][j] != 0:
                    tot += circles[i][j]
                    cnt += 1
        if cnt > 0:
            avg = tot / cnt
            for i in range(N):
                for j in range(M):
                    if circles[i][j] != 0:
                        if circles[i][j] > avg:
                            circles[i][j] -= 1
                        elif circles[i][j] < avg:
                            circles[i][j] += 1

answer = sum(sum(row) for row in circles)
print(answer)
