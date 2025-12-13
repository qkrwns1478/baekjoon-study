from collections import defaultdict

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fireballs = [list(map(int, input().split())) for _ in range(M)]

def check(s):
    t = {i % 2 for i in s}
    return len(t) == 1

for _ in range(K):
    # 파이어볼 이동
    D = defaultdict(set)
    for i in range(len(fireballs)):
        r, c, m, s, d = fireballs[i]
        nr = (r + dx[d] * s) % N
        nc = (c + dy[d] * s) % N
        if nr == 0: nr = N
        if nc == 0: nc = N
        D[(nr, nc)].add(i)
        fireballs[i][0] = nr
        fireballs[i][1] = nc

    # 2개 이상 있는 칸에서 파이어볼 합쳐지고 4개로 나뉨
    tmp = list()
    for r, c in D:
        if len(D[(r, c)]) == 1:
            tmp.append(fireballs[D[(r, c)].pop()])
        else:
            sum_m = 0
            sum_s = 0
            set_d = set()
            for i in D[(r, c)]:
                sum_m += fireballs[i][2]
                sum_s += fireballs[i][3]
                set_d.add(fireballs[i][4])
            new_m = sum_m // 5
            if new_m == 0:
                continue
            new_s = sum_s // len(D[(r, c)])
            new_d = [0, 2, 4, 6] if check(set_d) else [1, 3, 5, 7]
            for i in range(4):
                tmp.append([r, c, new_m, new_s, new_d[i]])
    fireballs = tmp

answer = sum(fireballs[i][2] for i in range(len(fireballs)))
print(answer)