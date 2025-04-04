import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    
    # dp[i] : c번째 동전 추가시 i원을 만드는 경우의 수
    dp = [0] * (m+1)
    dp[0] = 1
    for c in coin:
        for i in range(c, m+1):
            dp[i] += dp[i-c]

    print(dp[m])