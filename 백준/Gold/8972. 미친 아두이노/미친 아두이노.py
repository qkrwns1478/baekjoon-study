from collections import defaultdict

def draw_map():
    global jsx, jsy
    global ad
    for i in range(n):
        for j in range(m):
            if jsx == i and jsy == j:
                print('I', end='')
            elif (i, j) in ad and ad[(i, j)] > 0:
                print('R', end='')
            else:
                print('.', end='')
        print()

dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

n, m = map(int, input().split())
jsx, jsy = 0, 0
ad = defaultdict(int)

for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == 'I':
            jsx, jsy = i, j
        elif s[j] == 'R':
            ad[(i, j)] += 1

cmd = input()
cnt = 0
is_alive = True
for c in cmd:
    # 종수 이동
    cnt += 1
    nx = jsx + dx[int(c)]
    ny = jsy + dy[int(c)]
    if 0 <= nx < n and 0 <= ny < m:
        jsx, jsy = nx, ny
    if (jsx, jsy) in ad and ad[(jsx, jsy)] > 0:
        is_alive = False
        break

    # 아두이노 이동
    tmp = defaultdict(int)
    for adx, ady in ad:
        if ad[(adx, ady)] > 0:
            adi = 0
            if adx == jsx:
                if ady > jsy: adi = 4
                else: adi = 6
            elif adx > jsx:
                if ady > jsy: adi = 7
                elif ady < jsy: adi = 9
                else: adi = 8
            else:
                if ady > jsy: adi = 1
                elif ady < jsy: adi = 3
                else: adi = 2
            nax = adx + dx[adi]
            nay = ady + dy[adi]
            tmp[(nax, nay)] += 1
    ad = tmp
    for x, y in ad:
        if x == jsx and y == jsy:
            is_alive = False
            break
        elif ad[(x, y)] > 1:
            ad[(x, y)] = 0
    if not is_alive:
        break

if is_alive:
    draw_map()
else:
    print(f"kraj {cnt}")