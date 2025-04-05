import sys
input = sys.stdin.readline

n = int(input())
arr = list()
max_day = 0
for _ in range(n):
    p, d = map(int, input().split())
    arr.append((p, d))
    max_day = max(max_day, d)
arr.sort(key=lambda x: (-x[0], x[1]))

dp = [0] * (max_day+1)
for p, d in arr:
    for i in range(d, 0, -1):
        if dp[i] == 0:
            dp[i] = p
            break

print(sum(dp))