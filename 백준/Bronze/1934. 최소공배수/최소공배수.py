import sys
from math import lcm
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))