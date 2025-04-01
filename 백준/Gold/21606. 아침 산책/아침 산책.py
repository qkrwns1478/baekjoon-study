import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i):
    global answer
    
    if visited[i]:
        return

    visited[i] = True
    for j in adj[i][0]:
        if not visited[j]:
            if adj[j][1] == 0:
                dfs(j)
            else:
                answer += 1

n = int(input())
A = input() # 1 = 실내, 0 = 실외
adj = dict()
for i in range(1, n+1):
    adj[i] = (list(), int(A[i-1]))
    
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u][0].append(v)
    adj[v][0].append(u)

answer = 0
cnt = 0
for i in range(1, n+1):
    if adj[i][1] == 0:
        continue
    
    visited = [False] * (n+1)
    dfs(i)
    answer += 1
    cnt += 1

print(answer - cnt)