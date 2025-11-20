from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

days = 0
while True:
    union = defaultdict(set)
    visited = set()
    union_idx = 0
    flag = False

    def dfs(x, y, u):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    visited.add((nx, ny))
                    union[u].update({(x, y), (nx, ny)})
                    dfs(nx, ny, u)

    for r in range(N):
        for c in range(N):
            if (r, c) not in visited:
                dfs(r, c, union_idx)
                if len(union[union_idx]) == 0:
                    continue
                total = 0
                for x, y in union[union_idx]:
                    total += arr[x][y]
                total //= len(union[union_idx])
                for x, y in union[union_idx]:
                    arr[x][y] = total
                union_idx += 1
                flag = True

    if flag: days += 1
    else: break

print(days)