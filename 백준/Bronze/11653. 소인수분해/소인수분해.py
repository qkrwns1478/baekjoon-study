n = int(input())
d = 2
while n > 1:
    while n % d== 0:
        print(d)
        n //= d
    d += 1
