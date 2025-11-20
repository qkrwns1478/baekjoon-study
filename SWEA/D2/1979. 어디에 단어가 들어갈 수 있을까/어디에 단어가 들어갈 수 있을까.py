T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(input().split()) for _ in range(N)]
    answer = 0

    target = '1' * K
    for i in range(N):
        answer += ''.join(arr[i]).split('0').count(target)
        tmp = ''
        for j in range(N):
            tmp += arr[j][i]
        answer += tmp.split('0').count(target)

    '''
    dx = [1, 0]
    dy = [0, 1]
    visited = set()
    
    def check(x, y, d):
        if d == 0:
            if x+1 >= N: return True
            elif arr[x+1][y] == 0: return True
            else: return False
        else:
            if y+1 >= N: return True
            elif arr[x][y+1] == 0: return True
            else: return False

    def dfs(x, y, d, cur):
        if cur == K:
            if check(x, y, d):
                global answer
                answer += 1
            return
        for i in range(2):
            if i % 2 != d:
                continue
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and (nx, ny, d) not in visited:
                visited.add((nx, ny, d))
                dfs(nx, ny, d, cur + arr[nx][ny])

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                for d in range(2):
                    if (i, j, d) not in visited:
                        visited.add((i, j, d))
                        dfs(i, j, d, 1)
    '''

    print(f"#{t} {answer}")