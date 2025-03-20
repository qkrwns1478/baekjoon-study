n= int(input())
o = n
cnt = 0

for _ in range(100):
    b = n // 10 + n % 10
    n = (n % 10) * 10 + b % 10
    cnt += 1

    if n == o:
        break

print(cnt)