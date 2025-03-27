import sys
input = sys.stdin.readline
from itertools import permutations as permt

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if m == 1:
    for i in arr:
        print(i)
else:
    pmt = permt(arr, m)
    for p in pmt:
        print(*p)