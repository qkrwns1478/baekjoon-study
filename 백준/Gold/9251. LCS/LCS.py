import sys
input = sys.stdin.readline

'''
def LCS(i, j):
    if i == 0 or j == 0:
        return 0
    if A[i] == B[j]:
        return LCS(i-1, j-1) + 1
    else:
        return max(LCS(i-1, j), LCS(i, j-1))
'''

A = input()
B = input()
a, b = len(A), len(B)

dp = [[0] * (b+1) for _ in range(a+1)]
for i in range(1, a+1):
    for j in range(1, b+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[a][b]-1)