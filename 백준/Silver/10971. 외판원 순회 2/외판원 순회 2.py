def dfs(city, count, cost):
    global min_val

    if count == n:
        if w[city][0] > 0:
            min_val = min(min_val, cost + w[city][0])
        return

    for nc in range(n):
        if not visited[nc] and w[city][nc] > 0:
            visited[nc] = True
            dfs(nc, count+1, cost + w[city][nc])
            visited[nc] = False # 백트래킹

n = int(input())
w = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    w[i] = list(map(int, input().split()))
visited = [False] * n
min_val = float("inf")

visited[0] = True
dfs(0, 1, 0)
print(min_val)