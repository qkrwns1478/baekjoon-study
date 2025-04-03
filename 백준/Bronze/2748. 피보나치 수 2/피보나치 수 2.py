import sys
input = sys.stdin.readline

n = int(input())
dp = [-1] * (n+1)
dp[0] = 0
dp[1] = 1

def fibo(n):
    if dp[n] != -1: # 이미 계산된 값이 있는 경우
        return dp[n]
    dp[n] = fibo(n-2) + fibo(n-1) # memoization
    return dp[n]

fibo(n)
print(dp[n])