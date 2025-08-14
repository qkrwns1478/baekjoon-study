n = int(input())
a = 1
arr = list()
for _ in range(n):
    arr.append(a)
    a += 2
print(*arr)