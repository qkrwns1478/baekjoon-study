import sys
input = sys.stdin.readline

n = int(input())
adj = dict()
visited = [False] * (n+1)

for i in range(1, n+1):
    adj[i] = list()

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
            
def virus(key):
    global answer

    if visited[key]:
        return

    visited[key] = True
    answer += 1
    
    for i in adj[key]:
        virus(i)

answer = 0
virus(1)

print(answer-1)