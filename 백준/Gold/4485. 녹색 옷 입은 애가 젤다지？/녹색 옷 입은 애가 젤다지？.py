from heapq import heappush, heappop
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
idx = 1
while True:
    n = int(input())
    if n == 0: break
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))
    queue = list()
    heappush(queue, (arr[0][0], 0, 0))
    visited = set()
    visited.add((0, 0))
    while queue:
        k, x, y = heappop(queue)
        if x == n-1 and y == n-1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                heappush(queue, (k+arr[nx][ny], nx, ny))
                visited.add((nx, ny))
    print(f"Problem {idx}: {k}")
    idx += 1