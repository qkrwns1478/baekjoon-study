from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    Q_max = list()
    Q_min = list()
    k = int(input())
    visited = [False] * k
    for i in range(k):
        c, n = input().split()
        if c == 'I':
            # Q에 정수 n 삽입
            n = int(n)
            heappush(Q_max, (-n, i))
            heappush(Q_min, (n, i))
            visited[i] = True
        else:
            if n == '1':
                # Q에서 최대값 삭제
                while Q_max and not visited[Q_max[0][1]]:
                    heappop(Q_max)
                if Q_max:
                    visited[Q_max[0][1]] = False
                    heappop(Q_max)
            else:
                # Q에서 최소값 삭제
                while Q_min and not visited[Q_min[0][1]]:
                    heappop(Q_min)
                if Q_min:
                    visited[Q_min[0][1]] = False
                    heappop(Q_min)

    while Q_max and not visited[Q_max[0][1]]:
        heappop(Q_max)
    while Q_min and not visited[Q_min[0][1]]:
        heappop(Q_min)

    if not Q_max or not Q_min:
        print('EMPTY')
    else:
        print(-Q_max[0][0], Q_min[0][0])
