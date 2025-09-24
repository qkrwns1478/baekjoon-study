from math import ceil

n, k, l = map(int, input().split())
a, b = min(k, l), max(k, l)
ans = 0
while a != b:
    ans += 1
    a = ceil(a/2)
    b = ceil(b/2)
print(ans)