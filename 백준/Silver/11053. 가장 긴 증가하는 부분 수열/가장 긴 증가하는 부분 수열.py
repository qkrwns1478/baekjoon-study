import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
answer = 0

for i in range(n):
    tmp = 0
    for j in range(i):
        if arr[i] > arr[j]:
            tmp = max(tmp, dp[j])
    dp[i] = tmp + 1

    answer = max(answer, dp[i])

print(answer)