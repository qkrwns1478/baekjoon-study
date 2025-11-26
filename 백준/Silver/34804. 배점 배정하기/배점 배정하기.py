from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = set()
flag = True
for _ in range(N):
    tmp = list(map(int, input().split()))
    s = tuple(set(tmp[1:]))
    if s in arr:
        flag = False
        break
    arr.add(s)

if not flag:
    print(-1)
else:
    for i in range(1, M+1):
        print(2**(i-1), end=' ')