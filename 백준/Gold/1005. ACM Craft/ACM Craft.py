from collections import deque

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = deque(map(int, input().split()))
    D.appendleft(0)
    graph = [list() for _ in range(N+1)]
    indegree = [0] * (N+1)
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    W = int(input())

    dp = [0] * (N+1)
    queue = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = D[i]

    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            indegree[i] -= 1
            dp[i] = max(dp[cur] + D[i], dp[i])
            if indegree[i] == 0:
                queue.append(i)

    print(dp[W])