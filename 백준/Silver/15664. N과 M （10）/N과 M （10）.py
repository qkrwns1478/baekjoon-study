import sys
input = sys.stdin.readline
from itertools import combinations as comb

def 정상화(arr):
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    return arr

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if m == 1:
    arr = 정상화(arr)
    for i in arr:
        print(i)
else:
    cmb = comb(arr, m)
    cmb = 정상화(cmb)
    for c in cmb:
        print(*c)