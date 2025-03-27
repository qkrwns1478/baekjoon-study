import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement as comb

n, m = map(int, input().split())

if m == 1:
    for i in range(1, n+1):
        print(i)
else:
    cmb = comb(list(range(1, n+1)), m)
    for c in cmb:
        print(*c)