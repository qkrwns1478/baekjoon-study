import sys
t = int(input())
for _ in range(t):
    r, s = sys.stdin.readline().split()
    for i in range(len(s)):
        print(s[i] * int(r), end='')
    print()