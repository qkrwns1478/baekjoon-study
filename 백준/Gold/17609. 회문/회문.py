from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    s = input().strip()
    left = 0
    right = len(s) - 1
    res = 0
    while left < right:
        if s[left] != s[right]:
            a = s[left + 1:right + 1]
            if a == a[::-1]:
                res = 1
                break
            b = s[left:right]
            if b == b[::-1]:
                res = 1
                break
            if res == 0:
                res = 2
            break
        left += 1
        right -= 1
    print(res)