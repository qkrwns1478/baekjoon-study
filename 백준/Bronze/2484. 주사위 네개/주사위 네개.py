n = int(input())
max_val = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    a, b, c, d = arr[0], arr[1], arr[2], arr[3]
    del arr

    r = 0
    if a == b == c == d:
        r = 50000 + a * 5000

    elif a == b == c or b == c == d:
        r = 10000 + b * 1000

    elif a == b and c == d:
        r = 2000 + a * 500 + c * 500

    elif a == b or b == c:
        r = 1000 + b * 100
    elif c == d:
        r = 1000 + c * 100

    else:
        r = d * 100

    #print(max_val, r)
    max_val = max(max_val, r)

print(max_val)