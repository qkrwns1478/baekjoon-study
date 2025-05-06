dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFF(x, y, d, tmp):
    nx = x + dx[d]
    ny = y + dy[d]
    while (0 <= nx < n and 0 <= ny < n):
        if tmp[nx][ny] == -1: return True
        elif tmp[nx][ny] == 1: return False
        nx += dx[d]
        ny += dy[d]
    return True

def BF(a, b, c):
    global arr
    tmp = [[0] * n for _ in range(n)]
    teachers = list()
    for i in range(n):
        for j in range(n):
            if (i, j) in [a, b, c]: tmp[i][j] = -1
            else: tmp[i][j] = arr[i][j]
            if tmp[i][j] == 2: teachers.append((i, j))
    for x, y in teachers:
        for i in range(4):
            if not BFF(x, y, i, tmp):
                return False
    return True

def test(blank):
    for a in blank:
        for b in blank:
            for c in blank:
                if a != b and b != c and c != a:
                    if BF(a, b, c):
                        return True
    return False

n = int(input())
arr = [[0] * n for _ in range(n)]
blank = list()
for i in range(n):
    s = input().split()
    for j in range(n):
        if s[j] == 'S': arr[i][j] = 1
        elif s[j] == 'T': arr[i][j] = 2
        else: blank.append((i, j))
print("YES" if test(blank) else "NO")