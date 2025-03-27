import sys
input = sys.stdin.readline
from itertools import product

def 정상화(arr):
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    return arr

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if m == 1:
    for i in 정상화(arr):
        print(i)
else:
    pdt = product(arr, repeat = m)
    for p in 정상화(pdt):
        print(*p)