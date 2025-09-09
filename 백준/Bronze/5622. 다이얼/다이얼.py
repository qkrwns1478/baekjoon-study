def dial(c):
    if c in 'ABC':
        return 2
    elif c in 'DEF':
        return 3
    elif c in 'GHI':
        return 4
    elif c in 'JKL':
        return 5
    elif c in 'MNO':
        return 6
    elif c in 'PQRS':
        return 7
    elif c in 'TUV':
        return 8
    elif c in 'WXYZ':
        return 9
    else:
        return 0

s = input()
ans = 0
for c in s:
    ans += dial(c) + 1
print(ans)