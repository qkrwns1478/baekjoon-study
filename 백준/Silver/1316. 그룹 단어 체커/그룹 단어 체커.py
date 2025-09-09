import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    s = input().strip()
    flag = True
    cur = ''
    tmp = set()
    for c in s:
        if c not in tmp:
            tmp.add(c)
            cur = c
        elif c != cur:
            flag = False
            break
    if flag:
        ans += 1
print(ans)