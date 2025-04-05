import sys
input = sys.stdin.readline
from math import comb

t = int(input())
for _ in range(t):
    l = int(input())
    if l % 2 == 1:
        print(0)
    else:
        n = l//2
        print((comb(2*n, n) // (n+1)) % (10**9 + 7))