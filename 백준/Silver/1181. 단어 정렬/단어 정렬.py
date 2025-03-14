n = int(input())
arr = set()
for _ in range(n):
    arr.add(input())
arr = sorted(arr, key=lambda x: (len(x), x))
for i in range(len(arr)):
    print(arr[i])