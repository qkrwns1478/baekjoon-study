from itertools import combinations as comb

L, C = map(int, input().split())
arr = list(input().split())
vowels = {'a', 'e', 'i', 'o', 'u'}
vow = list()
con = list()
for a in arr:
    if a in vowels:
        vow.append(a)
    else:
        con.append(a)

words = list()
# 자음의 개수: 최소 2개 ~ 최대 L-1개
for i in range(2, L):
    cc = list(comb(con, i))
    cv = list(comb(vow, L-i))
    for tc in cc:
        for tv in cv:
            t = tc + tv
            t = sorted(list(t))
            words.append(''.join(t))

words.sort()
for w in words:
    print(w)