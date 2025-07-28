import sys
input = sys.stdin.readline
a, b = map(int, input().split())
A = set(map(int, input().split()))
B = list(map(int, input().split()))
n = 0
for i in B:
    if i in A:
        n += 1
print((a-n)+(b-n))