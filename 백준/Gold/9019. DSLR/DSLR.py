import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    a, b = map(int, input().split()) # 초기값, 최종값
    visited = [-1] * 10000
    queue = deque()
    queue.append(a)
    visited[a] = a
    log = [''] * 10000
    while queue:
        now = queue.popleft()
        if now == b:
            break
        
        valD = (2*now) % 10000
        valS = now - 1
        if valS == -1: valS = 9999
        valL = str(now).zfill(4)
        valL = valL[1:] + valL[0]
        valL = int(valL)
        valR = str(now).zfill(4)
        valR = valR[3] + valR[:3]
        valR = int(valR)

        if visited[valD] == -1:
            visited[valD] = now
            queue.append(valD)
            if not log[valD]:
                log[valD] =  "D"
        if visited[valS] == -1:
            visited[valS] = now
            queue.append(valS)
            if not log[valS]:
                log[valS] = "S"
        if visited[valL] == -1:
            visited[valL] = now
            queue.append(valL)
            if not log[valL]:
                log[valL] = "L"
        if visited[valR] == -1:
            visited[valR] = now
            queue.append(valR)
            if not log[valR]:
                log[valR] = "R"

    result = b
    answer = list()
    answer.append(log[b])
    while result != a:
        result = visited[result]
        answer.append(log[result])
    answer.reverse()
    print(*answer, sep='')