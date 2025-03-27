import sys
input = sys.stdin.readline
from itertools import product

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if m == 1:
    for i in arr:
        print(i)
else:
    pdt = product(arr, repeat = m)
    for p in pdt:
        print(*p)