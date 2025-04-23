import sys
input = sys.stdin.readline

m = int(input())
a = 0
b = 0
for _ in range(m):
    q = list(map(int, input().split()))
    if q[0] == 1:
        a += q[1]
        b ^= q[1]
    elif q[0] == 2:
        a -= q[1]
        b ^= q[1]
    elif q[0] == 3: print(a)
    else: print(b)