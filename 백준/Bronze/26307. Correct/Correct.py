import sys
input = sys.stdin.readline

h, m = map(int, input().split())
h -= 9
print(h*60 + m)