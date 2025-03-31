import sys
input = sys.stdin.readline

n = int(input())
arr = [[] * n for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = float("inf")

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(n):
    for j in range(n):
        if arr[i][j] < float("inf"):
            arr[i][j] = 1
        else:
            arr[i][j] = 0
    print(*arr[i])