for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    x_flag = 0
    if x2 < x3 or x1 > x4:
        x_flag = 1
    elif x2 == x3 or x1 == x4:
        x_flag = 2

    y_flag = 0
    if y2 < y3 or y1 > y4:
        y_flag = 1
    elif y2 == y3 or y1 == y4:
        y_flag = 2

    if x_flag == 0:
        if y_flag == 0:
            answer = 'a'
        elif y_flag == 1:
            answer = 'd'
        else:
            answer = 'b'
    elif x_flag == 1:
        answer = 'd'
    else:
        if y_flag == 0:
            answer = 'b'
        elif y_flag == 1:
            answer = 'd'
        else:
            answer = 'c'

    print(answer)
