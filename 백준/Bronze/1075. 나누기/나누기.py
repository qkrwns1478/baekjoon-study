n = int(input())
f = int(input())

m = (n // 100) * 100
for i in range(100):
    if (m+i) % f == 0:
        print("%02d" % i)
        break