from collections import defaultdict
n, p, q = map(int, input().split())

def calc(i):
    if i == 0:
        return 1
    if i in dp:
        return dp[i]
    dp[i] = calc(i//p) + calc(i//q)
    return dp[i]

dp = defaultdict(int)
print(calc(n))

'''A = [0] * (n+1)
A[0] = 1
for i in range(1, n+1):
    A[i] = A[i//p] + A[i//q]
print(A[n])'''