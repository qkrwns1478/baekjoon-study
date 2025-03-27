import sys
input = sys.stdin.readline
from itertools import product

n, m = map(int, input().split())

if m == 1:
    for i in range(1, n+1):
        print(i)
else:
    arr = list(range(1, n+1))
    pdt = product(arr, repeat = m)
    for p in pdt:
        print(*p)