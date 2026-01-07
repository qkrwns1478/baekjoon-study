from collections import deque

M, S = map(int, input().split(':'))
T = M * 60 + S

queue = deque()
queue.append((0, 0, False))
visited = set()
visited.add((0, False))
answer = float('inf')

dt = [600, 60, 30, 10]
dr = [False, False, True, False]

while queue:
    t, c, r = queue.popleft()
    if t == T:
        if r:
            answer = min(answer, c)
        else:
            answer = min(answer, c+1)
        continue
    if t > T:
        continue
    for i in range(4):
        nt = t + dt[i]
        nr = dr[i]
        if (nt, nr) not in visited:
            visited.add((nt, nr))
            queue.append((nt, c+1, nr))

print(answer)
