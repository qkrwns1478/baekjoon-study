from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    min_dist = float('inf')
    for k in range(1, N-1):
        cur_dist = 0
        queue = deque()
        for i in range(N):
            if i == k:
                continue
            queue.append(i)
            if len(queue) == 2:
                cur_dist += abs(X[queue[1]] - X[queue[0]])
                queue.popleft()
        min_dist = min(min_dist, cur_dist)
    print(min_dist)