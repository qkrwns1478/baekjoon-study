n = int(input())
max_x, max_y = -100, -100
min_x, min_y = 100, 100
for _ in range(n):
    ax, ay, bx, by = map(int, input().split())
    max_x = max(max_x, bx)
    max_y = max(max_y, by)
    min_x = min(min_x, ax)
    min_y = min(min_y, ay)
    print(2*(max_x - min_x + max_y - min_y))