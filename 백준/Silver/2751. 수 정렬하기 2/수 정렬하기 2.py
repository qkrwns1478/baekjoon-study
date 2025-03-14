import sys
n = int(sys.stdin.readline())
arr = list()
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for num in arr:
    print(num)