from collections import defaultdict
from sys import stdin
input = stdin.readline

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

shark_pos = defaultdict(set)
sharks = list()

R, C, M = map(int, input().split())
if M == 0:
    print(0)
    exit()

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append([r, c, s, d, z, True])
    shark_pos[(r, c)].add(i)

def turn(n):
    return n + 1 if n % 2 else n - 1

fishman = 0
answer = 0
while True:
    # 낚시왕 이동
    fishman += 1
    # print(f"현재 낚시왕 위치: {fishman}")
    if fishman > C:
        break
    # 낚시왕이 상어 잡음
    for i in range(1, R+1):
        if (i, fishman) not in shark_pos or len(shark_pos[(i, fishman)]) == 0:
            continue
        idx = shark_pos[(i, fishman)].pop()
        answer += sharks[idx][4]
        sharks[idx][5] = False
        # print(f"낚시왕이 {chr(idx+65)}번 상어 잡음")
        break
    # 상어 이동
    for i in range(len(sharks)):
        if not sharks[i][5]:
            continue
        x, y, s, d, z, _ = sharks[i]
        if s == 0:
            continue
        if d == 1 or d == 2:
            s %= (R - 1) * 2 if R > 1 else 1
        else:
            s %= (C - 1) * 2 if C > 1 else 1
        px, py, = x, y
        for _ in range(s):
            nx, ny = x + dx[d], y + dy[d]
            if not (1 <= nx <= R and 1 <= ny <= C):
                d = turn(d)
                nx, ny = x + dx[d], y + dy[d]
            x, y = nx, ny
        # print(f"{chr(i+65)}번 상어가 ({px}, {py})에서 ({x}, {y})로 이동")
        shark_pos[(px, py)].remove(i)
        shark_pos[(x, y)].add(i)
        sharks[i][0], sharks[i][1], sharks[i][3] = x, y, d
    # 상어끼리 잡아먹음
    for xy in shark_pos:
        if len(shark_pos[xy]) <= 1:
            continue
        max_z = 0
        max_i = 0
        cur_sharks = list(shark_pos[xy])
        for i in cur_sharks:
            if max_z < sharks[i][4]:
                max_z = sharks[i][4]
                max_i = i
        for i in cur_sharks:
            if i != max_i:
                shark_pos[xy].remove(i)
                sharks[i][5] = False
                # print(f"{chr(max_i+65)}번 상어가 {chr(i+65)}번 상어 잡아먹음")

print(answer)