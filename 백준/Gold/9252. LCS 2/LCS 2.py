import sys
sys.setrecursionlimit(10**4)

A = input()
B = input()
a, b = len(A), len(B)

dp = [[0] * (b+1) for _  in range(a+1)]
for i in range(1, a+1):
    for j in range(1, b+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[-1][-1])

def LCS(i, j):
    if i == 0 or j == 0:
        return
    if A[i-1] == B[j-1]:
        answer.append(A[i-1])
        LCS(i-1, j-1)
    else:
        if dp[i-1][j] > dp[i][j-1]:
            LCS(i-1, j)
        else:
            LCS(i, j-1)

answer = list()
LCS(a, b)
answer.reverse()
print(''.join(answer))