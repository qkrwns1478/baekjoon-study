import sys
input = sys.stdin.readline
from math import gcd

n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

A, B = 1, 1
for i in range(n):
    A *= N[i]
for i in range(m):
    B *= M[i]

answer = gcd(A, B)
if answer > 999999999:
    print(str(answer % (10**9)).zfill(9))
else:
    print(answer)