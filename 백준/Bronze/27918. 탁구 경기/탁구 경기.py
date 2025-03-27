import sys
input = sys.stdin.readline

n = int(input())
d, p = 0, 0
for _ in range(n):
    s = input().strip()
    if s == "D":
        d += 1
    else:
        p += 1
    if abs(d-p) >= 2:
        break
print(f"{d}:{p}")