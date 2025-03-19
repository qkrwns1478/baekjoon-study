def hanoi(n, s, e):
    m = 6 - s - e
    if n > 1: hanoi(n-1, s, m)
    print(s, e)
    if n > 1: hanoi(n-1, m, e)

n = int(input())
print(2**n - 1)
hanoi(n, 1, 3)