import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

n = int(input())
adj = dict()
for i in range(1, n+1):
    adj[i] = list()

place = list("0" + input().strip())
    
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(i):
    cnt = 0
    visited[i] = True
    for j in adj[i]:
        if not visited[j]:
            if place[j] == "1": # 실내에 도착하면 종료
                cnt += 1
            else:
                cnt += dfs(j)
    return cnt      

answer = 0
for i in range(1, n+1):
    if place[i] == "0":
        continue
    visited = [False] * (n+1)
    for j in range(i):
        if place[j] == "1":
            visited[j] = True
    if not visited[i]:
        answer += dfs(i)

print(answer*2)