import sys
h, m = map(int, sys.stdin.readline().split())
m -= 45
if m < 0:
    m += 60
    h -= 1
if h < 0:
    h += 24
print(h, m)