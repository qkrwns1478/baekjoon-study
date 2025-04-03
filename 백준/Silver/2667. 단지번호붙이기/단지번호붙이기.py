# 이전에 백준에 제출한 기록이 있지만 다시 작성했습니다.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= n-1:
            if not visited[nx][ny] and arr[nx][ny] == 1:
                dfs(nx, ny)

answer = 0
result = list()
for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)
            answer += 1
print(answer)
result.sort()
print(*result)