from sys import stdin
input = stdin.readline

S, P = map(int, input().split())
ans = 0
if S == P:
    ans = 1
else:
    flag = False
    for i in range(2, 10**6):
        if (S / i) ** i >= P:
            flag = True
            ans = i
            break
    if not flag:
        ans = -1
print(ans)