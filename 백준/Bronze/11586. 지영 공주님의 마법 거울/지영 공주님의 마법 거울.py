n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

k = int(input())
if k == 1:
    for i in range(n):
        print(arr[i])
elif k == 2:
    for i in range(n):
        print(arr[i][::-1])
else:
    for i in range(1, n+1):
        print(arr[n-i])