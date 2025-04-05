import sys
sys.setrecursionlimit(10**6)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                dfs(j)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer