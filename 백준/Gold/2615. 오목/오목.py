# ↖ ↑ ↗ → / ↘ ↓ ↙ ←
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

A = [list(map(int, input().split())) for _ in range(19)]

def sol(x, y, p, d, arr):
    if A[x][y] != p:
        return arr
    arr.append((x, y))
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < 19 and 0 <= ny < 19:
        return sol(nx, ny, p, d, arr)
    else:
        return arr

def solve():
    for i in range(19):
        for j in range(19):
            if A[i][j] in (1, 2):
                for d in range(4):
                    res1 = sol(i, j, A[i][j], d, [])
                    res2 = sol(i, j, A[i][j], d+4, [])
                    if len(res2) > 1:
                        res1 += res2[1:]
                    if len(res1) == 5:
                        res1.sort(key=lambda x: x[1])
                        print(A[i][j])
                        print(res1[0][0] + 1, res1[0][1] + 1)
                        return True
    return False

if not solve():
    print(0)
