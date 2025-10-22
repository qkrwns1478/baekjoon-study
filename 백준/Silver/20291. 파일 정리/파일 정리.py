from collections import defaultdict

n = int(input())
d = defaultdict(int)
for _ in range(n):
    _, ext = input().split('.')
    d[ext] += 1

for ext in sorted(d.keys()):
    print(ext, d[ext])