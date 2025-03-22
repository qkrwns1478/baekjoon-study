n = int(input())
for _ in range(n):
    i = int(input())
    if abs(i) % 2 == 1:
        print(i, "is odd")
    else:
        print(i, "is even")