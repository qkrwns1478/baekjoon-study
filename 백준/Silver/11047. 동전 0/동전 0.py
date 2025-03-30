n, k = map(int, input().split())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())

answer = 0
for i in range(n-1, -1, -1):
    if arr[i] <= k:
        answer += k // arr[i]
        k %= arr[i]

print(answer)