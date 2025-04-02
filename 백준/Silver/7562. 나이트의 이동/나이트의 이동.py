import sys
input = sys.stdin.readline
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

t = int(input())
for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    if sx == ex and sy == ey:
        print(0)
    else:
        queue = deque()
        queue.append((sx, sy, 0))
        visited = set()
        visited.add((sx, sy))
        while queue:
            x, y, cnt = queue.popleft()
            if x == ex and y == ey:
                print(cnt)
                break
            #visited.add((x,y))
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx <= l-1 and 0 <= ny <= l-1:
                    if (nx, ny) not in visited:
                        queue.append((nx, ny, cnt+1))
                        visited.add((nx, ny))