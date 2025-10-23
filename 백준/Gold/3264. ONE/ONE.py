n, s = map(int, input().split())
adj = [[] for _ in range(n+1)]
dist = [-1] * (n+1)

total = 0
for _ in range(n-1):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
    total += w

def dfs(cur):
    global max_dist
    max_dist = max(max_dist, dist[cur])
    for nxt, w in adj[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + w
            dfs(nxt)

dist[s] = 0
max_dist = 0
dfs(s)

res = 2 * total - max_dist
print(res)