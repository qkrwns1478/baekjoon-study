import sys
input = sys.stdin.readline
from itertools import permutations as permt

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if m == 1:
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    for i in arr:
        print(i)
else:
    pmt = permt(arr, m)
    pmt = set(pmt)
    pmt = list(pmt)
    pmt.sort()
    for p in pmt:
        print(*p)