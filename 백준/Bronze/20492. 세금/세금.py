import sys
input = sys.stdin.readline

n = int(input())
a = int(n - 0.22 * n)
b = int(n - 0.20 * 0.22 * n)
print(a, b)