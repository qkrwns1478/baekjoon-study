from collections import deque

arr = [deque() for _ in range(6)]
for _ in range(12):
    tmp = input()
    for i in range(6):
        arr[i].append(tmp[i])

answer = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    '''
    visited = set()
    puyo = set()
    
    def dfs(x, y, p, cnt):
        print(arr[x][y], cnt, x, y, p)
        if cnt >= 4:
            puyo.update(p)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 6 and 0 <= ny < 12 and arr[nx][ny] == arr[x][y] and (nx, ny) not in visited:
                visited.add((nx, ny))
                dfs(nx, ny, p | {(nx, ny)}, cnt+1)
    
    for i in range(6):
        if arr[i][-1] == '.':
            continue
        for j in range(11, -1, -1):
            if arr[i][j] != '.' and (i, j) not in visited:
                visited.add((i, j))
                dfs(i, j, {(i, j)}, 1)
    '''

    def bfs(x, y):
        queue = deque([(x, y)])
        visited.add((x, y))
        puyo = {(x, y)}

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 6 and 0 <= ny < 12 and arr[nx][ny] == arr[x][y] and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    puyo.add((nx, ny))

        return puyo

    flag = False
    visited = set()
    for i in range(6):
        for j in range(12):
            if arr[i][j] != '.' and (i, j) not in visited:
                puyo = bfs(i, j)
                if len(puyo) >= 4:
                    flag = True
                    while puyo:
                        x, y = puyo.pop()
                        arr[x][y] = '.'

    if not flag:
        break


    for i in range(6):
        # if arr[i] == deque(['.'] * 12):
        #     continue
        # while arr[i][-1] == '.':
        #     arr[i].rotate(1)
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if arr[i][j] != '.' and arr[i][k] == '.':
                    arr[i][k] = arr[i][j]
                    arr[i][j] = '.'
    answer += 1

print(answer)
