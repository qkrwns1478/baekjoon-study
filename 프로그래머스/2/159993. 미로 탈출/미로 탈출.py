from collections import deque
def solution(maps):
    answer = float("inf")
    n = len(maps)
    m = len(maps[0])
    sx, sy = 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                sx, sy = i, j
                break
    
    visited = set()
    visited.add((sx, sy))
    queue = deque()
    queue.append((sx, sy, 0))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    flag = False
    while queue:
        x, y, time = queue.popleft()
        if maps[x][y] == 'L':
            flag = True
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if maps[nx][ny] != 'X' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, time+1))
    
    if not flag:
        return -1
    
    visited = set()
    visited.add((x, y))
    queue.clear()
    queue.append((x, y, time))
    while queue:
        x, y, time = queue.popleft()
        if maps[x][y] == 'E':
            answer = time
            break
        visited.add((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if maps[nx][ny] != 'X' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, time+1))
        
    return answer if answer < float("inf") else -1