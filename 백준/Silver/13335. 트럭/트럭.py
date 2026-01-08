from collections import deque

n, w, L = map(int, input().split())
a = list(map(int, input().split()))

queue = deque([0 for _ in range(w)])
answer = 0
i = 0

while i < n:
    answer += 1
    queue.popleft()
    if sum(queue) + a[i] <= L:
        queue.append(a[i])
        i += 1
    else:
        queue.append(0)

print(answer + len(queue))
