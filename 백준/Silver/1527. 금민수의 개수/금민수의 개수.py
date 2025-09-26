from itertools import product

a, b = input().split()
la, lb = len(a), len(b)
ans = 0

for i in range(la, lb+1):
    pro = product(['4', '7'], repeat=i)
    if la == lb:
        for p in pro:
            x = int(''.join(p))
            if int(a) <= x <= int(b):
                ans += 1
    elif i == la:
        for p in pro:
            x = int(''.join(p))
            if x >= int(a):
                ans += 1
    elif i == lb:
        for p in pro:
            x = int(''.join(p))
            if x <= int(b):
                ans += 1
    else:
        ans += len(list(pro))

print(ans)