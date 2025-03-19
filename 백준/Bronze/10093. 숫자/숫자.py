a, b = map(int, input().split())

if a == b:
    print(0)

else:
    m = min(a, b) + 1
    n = max(a, b) - 1

    print(len(range(m, n+1)))

    for i in range(m, n+1):
        print(i, end=' ')