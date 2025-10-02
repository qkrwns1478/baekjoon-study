from sys import stdin
input = stdin.readline

n = int(input())
tmp = list()
l, r = 1, n

while l <= r:
    if l == r:
        tmp.append(l)
        break
    tmp.append(l)
    l += 1
    tmp.append(r)
    r -= 1

ans = tmp[::-1]
print(*ans)