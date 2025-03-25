n = int(input())
arr = list()
for i in range(1, n+1):
    if n % i == 0:
        arr.append(i)
print(sum(arr)*5 - 24)