import sys
input = sys.stdin.readline
n = int(input())
MOD = 10**9 + 7
a, b = 3, 5
for i in range(6, n+1):
    a, b = b, (a+b) % MOD
print(b, n-2)