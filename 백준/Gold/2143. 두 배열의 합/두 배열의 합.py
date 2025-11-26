from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

d = defaultdict(int)
for i in range(n):
    cur = 0
    for j in range(i, n):
        cur += A[j]
        d[cur] += 1

ans = 0
for i in range(m):
    cur = 0
    for j in range(i, m):
        cur += B[j]
        if T-cur in d:
            ans += d[T-cur]

print(ans)