import sys
input = sys.stdin.readline

def alp(x, y):
    return ord(arr[x][y]) - 65

r, c = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
arr = [list(input().strip()) for _ in range(r)]
visited = [False] * 26
visited[alp(0, 0)] = True

def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= r-1 and 0 <= ny <= c-1:
            if not visited[alp(nx, ny)]:
                visited[alp(nx, ny)] = True
                dfs(nx, ny, cnt+1)
                visited[alp(nx, ny)] = False

answer = float("-inf")
dfs(0, 0, 1)
print(answer)