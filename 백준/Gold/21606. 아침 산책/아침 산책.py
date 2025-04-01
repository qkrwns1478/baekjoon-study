import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from math import perm

n = int(input())
adj = [[] for _ in range(n+1)]
inout = list("0" + input().strip())
answer = 0

for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    if inout[a] == "1" and inout[b] == "1": # 연결된 두 노드가 실내-실내인 경우
        answer += 2
        
def dfs(i):
    cnt = 0
    visited[i] = True
    for j in adj[i]:
        if not visited[j]:
            if inout[j] == "1":
                cnt += 1
            else:
                cnt += dfs(j)
    return cnt      

visited = [False] * (n+1)
for i in range(1, n+1):
    if inout[i] == "0":
        if not visited[i]:
            r = dfs(i)
            answer += perm(r, 2) # 실외와 연결된 r개의 실내 중 2개를 선택하는 경우의 수

print(answer)