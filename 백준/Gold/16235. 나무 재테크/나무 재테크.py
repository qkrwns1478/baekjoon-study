from collections import defaultdict, deque
from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())

# G: N*N 땅 각 칸의 양분의 양
G = [[5] * n for _ in range(n)]

# A: 겨울에 각 칸에 추가되는 양분의 양
A = [list(map(int, input().split())) for _ in range(n)]

# namus: 각 칸에 있는 나무들
namus = defaultdict(deque)
for _ in range(m):
    x, y, z = map(int, input().split())
    namus[(x-1, y-1)].append(z)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for _ in range(k):
    # 봄 + 여름
    for cord in namus:
        x, y = cord
        namu_list = namus[(x, y)]
        tmp = deque()
        new_src = 0
        while namu_list:
            age = namu_list.popleft()
            if G[x][y] >= age:
                G[x][y] -= age
                tmp.append(age+1)
            else:
                new_src += age // 2
                while namu_list:
                    new_src += namu_list.popleft() // 2
                break
        namus[(x, y)] = tmp
        G[x][y] += new_src

    # 가을
    tmp = list()
    for cord in namus:
        x, y = cord
        namu_list = namus[(x, y)]
        for age in namu_list:
            if age % 5 == 0:
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        tmp.append((nx, ny))
    for x, y in tmp:
        namus[(x, y)].appendleft(1)

    # 겨울
    for i in range(n):
        for j in range(n):
            G[i][j] += A[i][j]

answer = 0
for cord in namus:
    answer += len(namus[cord])
print(answer)