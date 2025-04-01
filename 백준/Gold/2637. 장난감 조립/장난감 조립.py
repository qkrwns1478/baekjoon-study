import sys
input = sys.stdin.readline
from collections import deque

# 1~n-1 : 기본부품 or 중간부품
# n : 완제품
n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
D = [0] * (n+1)
base = list() # 기본부품 리스트

for _ in range(m):
    # x를 만드는데 y가 k개 필요하다
    x, y, k = map(int, input().split())
    adj[x].append((y, k))
    D[y] += 1

queue = deque()
for i in range(1, n+1):
    if not adj[i]:
        base.append(i)
    else:
        adj[i].sort()
    if D[i] == 0:
        queue.append(i)
    #print(f"{i} : {adj[i]}")

base.sort()
result = [0] * (n+1)
while queue:
    now = queue.popleft()
    k = result[now]
    for i, j in adj[now]: # 부품, 개수
        result[i] += j * (k or 1)
        D[i] -= 1
        if D[i] == 0:
            queue.append(i)
            
for i in base:
    print(i, result[i])