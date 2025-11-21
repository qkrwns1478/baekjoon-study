N = int(input())

def get_queen_range(x, y, flag=True):
    f = 1 if flag else -1
    for i in range(N):
        arr[x][i] += f
        arr[i][y] += f
        if 0 <= x-i and 0 <= y-i: arr[x-i][y-i] += f
        if x+i < N and y+i < N: arr[x+i][y+i] += f
        if 0 <= x-i and y+i < N: arr[x-i][y+i] += f
        if x+i < N and 0 <= y-i: arr[x+i][y-i] += f

def dfs(x, y):
    if arr[x][y] > 0:
        return 0
    if y == N-1 and arr[x][y] == 0:
        return 1

    res = 0
    get_queen_range(x, y)
    for i in range(N):
        res += dfs(i, y+1)
    get_queen_range(x, y, False)
    return res

ans = 0
arr = [[0] * N for _ in range(N)]
for i in range(N):
    ans += dfs(i, 0)
print(ans)
