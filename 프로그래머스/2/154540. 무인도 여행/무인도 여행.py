import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    n = len(maps)
    m = len(maps[1])
    arr = [[] for _ in range(n)]
    for i in range(n):
        arr[i] = list(maps[i])
    
    def dfs(i, j):
        visited[i][j] = True
        foods = int(arr[i][j])
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if not visited[nx][ny] and arr[nx][ny].isdigit():
                    foods += dfs(nx, ny)
        return foods
    
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j].isdigit():
                answer.append(dfs(i, j))
                
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer