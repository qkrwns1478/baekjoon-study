from collections import deque

n = int(input())
arr = deque(int(input()) for _ in range(n))
arr.appendleft(0)
dp = [0] * (n+1)

dp[1] = arr[1]
if n >= 2:
    dp[2] = arr[1] + arr[2]
if n >= 3:
    for i in range(3, n+1):
        dp[i] = max(arr[i-1] + dp[i-3], dp[i-2]) + arr[i]
print(dp[n])