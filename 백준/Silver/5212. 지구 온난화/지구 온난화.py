R, C = map(int, input().split())
A = [list(input()) for _ in range(R)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
B = [['.'] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if A[i][j] == 'X':
            cnt = 0
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < R and 0 <= nj < C and A[ni][nj] == 'X':
                    cnt += 1
            if cnt > 1:
                B[i][j] = 'X'

def transpose(arr):
    return [list(row) for row in zip(*arr)]

D = list()
s, e = 0, R-1
for i in range(R):
    if 'X' in B[i]:
        s = i
        break
for i in range(R-1, -1, -1):
    if 'X' in B[i]:
        e = i
        break
for i in range(s, e+1):
    D.append(B[i])

D = transpose(D)
E = list()
s, e = 0, C-1
for i in range(C):
    if 'X' in D[i]:
        s = i
        break
for i in range(C-1, -1, -1):
    if 'X' in D[i]:
        e = i
        break
for i in range(s, e+1):
    E.append(D[i])

E = transpose(E)
for i in range(len(E)):
    print(*E[i], sep='')
