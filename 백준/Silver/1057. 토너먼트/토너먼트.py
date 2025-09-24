def promote(x):
    if x % 2 == 0:
        return x // 2
    else:
        return (x+1) // 2

n, kim, lee = map(int, input().split())
a, b = min(kim, lee), max(kim, lee)
ans = 1
while True:
    if not (b-a == 1 and a % 2 == 1):
        ans += 1
        a = promote(a)
        b = promote(b)
        if n % 2 == 0:
            n //= 2
        else:
            n = n//2 + 1
    else:
        print(ans)
        break