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
                #print(f"{i} -> {j}")
                dfs(j)
            else:
                #print(f"{j}에서 종료")
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
    adj[u][0].sort()
    adj[v][0].sort()

#for i in range(1, n+1):
#    print(f"{i} : {adj[i]}")

answer = 0
cnt = 0
for i in range(1, n+1):
    if adj[i][1] == 0:
        continue
    
    visited = [False] * (n+1)
    #print(f"{i}에서 시작")
    dfs(i)
    answer += 1
    cnt += 1

print(answer - cnt)