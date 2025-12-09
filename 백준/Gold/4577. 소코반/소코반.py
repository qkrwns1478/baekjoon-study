dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def print_array(arr):
    for i in range(R):
        for j in range(C):
            cur = arr[i][j]
            if [i, j] in boxes:
                box_idx = boxes.index([i, j])
                cur = 'B' if box_valid[box_idx] else 'b'
            elif wx == i and wy == j:
                cur = 'W' if (i, j) in goals else 'w'
            elif (i, j) in goals:
                cur = '+'
            print(cur, end='')
        print()

t = 1
while True:
    R, C = map(int, input().split())
    if R == C == 0:
        break

    arr = [['.'] * C for _ in range(R)]
    boxes = list()
    box_valid = list()
    goals = set()
    wx, wy = 0, 0

    for i in range(R):
        s = input()
        for j in range(C):
            if s[j] == '#':
                arr[i][j] = '#'
            elif s[j] in ('W', 'w'):
                wx, wy = i, j
                if s[j] == 'W':
                    goals.add((i, j))
            elif s[j] == 'b':
                boxes.append([i, j])
                box_valid.append(False)
            elif s[j] == 'B':
                boxes.append([i, j])
                box_valid.append(True)
                goals.add((i, j))
            elif s[j] == '+':
                goals.add((i, j))

    def get_next_pos(x, y, d):
        if d == 'U':
            idx = 0
        elif d == 'D':
            idx = 1
        elif d == 'L':
            idx = 2
        else:
            idx = 3
        return x + dx[idx], y + dy[idx]

    cmd = input()
    flag = False
    for c in cmd:
        nx, ny = get_next_pos(wx, wy, c)
        if not (0 <= nx < R and 0 <= ny < C):
            continue
        elif arr[nx][ny] == '#':
            continue
        elif [nx, ny] in boxes:
            box_idx = boxes.index([nx, ny])
            bx, by = boxes[box_idx]
            nbx, nby = get_next_pos(bx, by, c)
            if not (0 <= nbx < R and 0 <= nby < C):
                continue
            elif arr[nbx][nby] == '#':
                continue
            elif [nbx, nby] in boxes:
                continue
            box_valid[box_idx] = (nbx, nby) in goals
            boxes[box_idx] = [nbx, nby]
        wx, wy = nx, ny

        # print(c)
        # print_array(arr)

        if False not in box_valid:
            flag = True
            break

    print(f"Game {t}: {'complete' if flag else 'incomplete'}")
    print_array(arr)
    t += 1
