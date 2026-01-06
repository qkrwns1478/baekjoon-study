K = int(input())
for k in range(1, K+1):
    M, N, P = map(int, input().split())
    score = [[0, 0, i] for i in range(P+1)]
    submitted = [[[0, False] for _ in range(M)] for _ in range(P+1)]
    for _ in range(N):
        p, m, t, j = input().split()
        p, t, j = int(p), int(t), int(j)
        m = ord(m) - 65
        if submitted[p][m][1]:
            continue
        if j == 0:
            submitted[p][m][0] += 1
        else:
            submitted[p][m][1] = True
            score[p][0] += t + submitted[p][m][0] * 20
            score[p][1] += 1
    score.sort(key=lambda x: (-x[1], x[0]))
    print(f"Data Set {k}:")
    for i in range(P+1):
        if score[i][2] == 0:
            continue
        print(score[i][2], score[i][1], score[i][0])
    if k != K:
        print()
