from collections import deque

gears = [None]
for _ in range(4):
    s = input()
    gears.append(deque(int(c) for c in s))

K = int(input())
for _ in range(K):
    g, d = map(int, input().split())
    # 현재 톱니 회전
    prev_g2 = gears[g][2]
    prev_g6 = gears[g][6]
    gears[g].rotate(d)
    # 왼쪽으로 이동하면서 톱니 회전하는지 확인
    cur_g, cur_d = g, d
    while cur_g > 1:
        if prev_g6 == gears[cur_g - 1][2]:
            break
        cur_g -= 1
        cur_d *= -1
        prev_g6 = gears[cur_g][6]
        gears[cur_g].rotate(cur_d)
    # 오른쪽으로 이동하면서 톱니 회전하는지 확인
    cur_g, cur_d = g, d
    while cur_g < 4:
        if prev_g2 == gears[cur_g+1][6]:
            break
        cur_g += 1
        cur_d *= -1
        prev_g2 = gears[cur_g][2]
        gears[cur_g].rotate(cur_d)

answer = sum(gears[i][0] * 2**(i-1) for i in range(1, 5))
print(answer)
