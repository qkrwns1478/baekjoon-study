n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(i, j):
    stack = list()
    stack.append((i, j))
    visited = [-1] * (n+1)
    visited[i] = j
    
    while stack:
        cur, w = stack.pop()
        for a, b in graph[cur]:
            if visited[a] == -1:
                visited[a] = b + w
                stack.append((a, visited[a]))

    max_val = max(visited)
    return (max_val, visited.index(max_val))

index = dfs(1, 0)[1]
print(dfs(index, 0)[0])