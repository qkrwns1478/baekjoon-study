from sys import stdin
input = stdin.readline

arr = list()
zeros = list()
for i in range(9):
    tmp = list(input().strip())
    for j in range(9):
        tmp[j] = int(tmp[j])
        if tmp[j] == 0:
            zeros.append((i, j))
    arr.append(tmp)

def is_valid(x, y, n):
    if n in arr[x]:
        return False
    for i in range(9):
        if arr[i][y] == n:
            return False
    hx, hy = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if arr[hx+i][hy+j] == n:
                return False
    return True

def dfs(z):
    if z == len(zeros):
        for i in range(9):
            print(*arr[i], sep='')
        exit()

    x, y = zeros[z]
    for i in range(1, 10):
        if is_valid(x, y, i):
            arr[x][y] = i
            dfs(z+1)
            arr[x][y] = 0

dfs(0)