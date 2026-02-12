from itertools import combinations_with_replacement as comb

N, M = map(int, input().split())
s1 = set(i for i in range(1, N+1, 1))
s2 = set(i for i in range(1, N+1, 2))
s3 = set(i for i in range(2, N+1, 2))
s4 = set(i for i in range(1, N+1, 3))

s = [s1, s2, s3, s4]
l = [len(s1), len(s2), len(s3), len(s4)]
answer = set()
answer.add(0)

for i in range(1, 5):
    cmbs = comb([0, 1, 2, 3], i)
    for cmb in cmbs:
        t = sum(l[c] for c in cmb)
        if t > M:
            continue
        cur = 0
        for c in cmb:
            for j in s[c]:
                cur ^= 2 << j
        answer.add(cur)

print(len(answer))
