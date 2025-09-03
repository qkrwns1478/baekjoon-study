from collections import deque

n, k = map(int, input().split())
dqs = [deque() for _ in range(19)]
cnt = 0

for i in range(n):
    name = input()
    j = len(name) - 2
    while dqs[j] and dqs[j][0] < i - k:
        dqs[j].popleft()
    cnt += len(dqs[j])
    dqs[j].append(i)

print(cnt)