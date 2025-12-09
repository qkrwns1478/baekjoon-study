from collections import defaultdict

def transpose(arr):
    return [list(row) for row in zip(*arr)]

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

answer = 0
while answer < 100:
    R, C = len(A), len(A[0])
    if R >= r and C >= c and A[r - 1][c - 1] == k:
        break
    tmp = list()
    if R >= C:
        for i in range(R):
            D = defaultdict(int)
            for j in range(C):
                if A[i][j] > 0:
                    D[A[i][j]] += 1
            tmp.append(sorted(D.items(), key=lambda x: (x[1], x[0])))
    else:
        for j in range(C):
            D = defaultdict(int)
            for i in range(R):
                if A[i][j] > 0:
                    D[A[i][j]] += 1
            tmp.append(sorted(D.items(), key=lambda x: (x[1], x[0])))

    max_len = 0
    for i in range(len(tmp)):
        max_len = max(max_len, len(tmp[i]))
    max_len *= 2
    max_len = min(max_len, 100)

    new_A = list()
    for i in range(len(tmp)):
        tmp_arr = list()
        for j in range(len(tmp[i])):
            tmp_arr.append(tmp[i][j][0])
            tmp_arr.append(tmp[i][j][1])
        while len(tmp_arr) < max_len:
            tmp_arr.append(0)
        if len(tmp_arr) > 100:
            tmp_arr = tmp_arr[:100]
        new_A.append(tmp_arr)

    if R >= C:
        A = new_A
    else:
        A = transpose(new_A)
    answer += 1
    # print(answer)
    # for i in range(len(A)):
    #     print(*A[i])

if answer >= 100 and (len(A) < r or len(A[0]) < c or A[r-1][c-1] != k):
    answer = -1
print(answer)