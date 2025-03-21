import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = set()
d = deque()

for _ in range(n):
    s = input().strip()
    a.add(s)
    
for _ in range(m):
    s = input().strip()
    if s in a:
        d.append(s)

print(len(d))
for people in sorted(d):
    print(people)