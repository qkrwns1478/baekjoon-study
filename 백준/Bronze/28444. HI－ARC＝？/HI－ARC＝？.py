import sys
input = sys.stdin.readline

h, i, a, r, c = map(int, input().split())
print(h * i - a*r*c)