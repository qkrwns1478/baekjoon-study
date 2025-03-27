import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement as comb

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if m == 1:
    for i in arr:
        print(i)
else:
    cmb = comb(arr, m)
    for c in cmb:
        print(*c)