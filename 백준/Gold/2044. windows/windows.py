N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = set()

def define_window(sx, sy):
    h = w = 1
    x, y = sx, sy
    name = ''
    while True:
        y += 1
        w += 1
        if arr[sx][y] == '+':
            ey = y
            break
        elif arr[sx][y] not in ('-', '|'):
            name += arr[sx][y]
    while True:
        x += 1
        h += 1
        if arr[x][sy] == '+':
            ex = x
            break
    visited.update({(sx, sy), (sx, ey), (ex, sy), (ex, ey)})
    return name, w, h

windows = list()
for i in range(N):
    for j in range(M):
        if arr[i][j] == '+' and (i, j) not in visited:
            windows.append(define_window(i, j))


windows.sort(key=lambda x:x[0])
# print(windows)

new_arr = [['.'] * M for _ in range(N)]
for n in range(len(windows)):
    name, w, h = windows[n]
    # print title
    dash = w - 4 - len(name)
    if dash % 2 == 0:
        ld = rd = dash // 2
    else:
        ld = dash // 2
        rd = ld + 1
    y = n
    new_arr[n][y] = '+'
    for _ in range(ld):
        y += 1
        new_arr[n][y] = '-'
    y += 1
    new_arr[n][y] = '|'
    for c in name:
        y += 1
        new_arr[n][y] = c
    y += 1
    new_arr[n][y] = '|'
    for _ in range(rd):
        y += 1
        new_arr[n][y] = '-'
    y += 1
    new_arr[n][y] = '+'
    # print body
    x, y = n+1, n
    for i in range(h-2):
        for j in range(w):
            if j == 0 or j == w-1:
                new_arr[x+i][y+j] = '|'
            else:
                new_arr[x+i][y+j] = '.'
    # print footer
    x, y = n+h-1, n
    for j in range(w):
        if j == 0 or j == w - 1:
            new_arr[x][y+j] = '+'
        else:
            new_arr[x][y+j] = '-'

for i in range(N):
    print(*new_arr[i], sep='')
