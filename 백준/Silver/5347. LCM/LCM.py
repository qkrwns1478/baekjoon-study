import sys
input = sys.stdin.readline
from math import lcm

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))