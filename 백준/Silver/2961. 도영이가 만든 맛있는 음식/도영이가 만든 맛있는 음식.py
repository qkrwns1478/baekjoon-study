from itertools import combinations as comb

N = int(input())
S = list()
B = list()
for _ in range(N):
    s, b = map(int, input().split())
    S.append(s)
    B.append(b)

answer = float('inf')
for i in range(1, N+1):
    cmbs = comb(range(N), i)
    for cmb in cmbs:
        cur_S, cur_B = 1, 0
        for j in cmb:
            cur_S *= S[j]
            cur_B += B[j]
        answer = min(answer, abs(cur_S - cur_B))

print(answer)
