n = int(input())

def solution():
    arr = [int(input()) for _ in range(n)]
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2, n):
        dp[i] = max(dp[i-1], arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2])
    print(dp[-1])

if n == 1:
    print(int(input()))
else:
    solution()