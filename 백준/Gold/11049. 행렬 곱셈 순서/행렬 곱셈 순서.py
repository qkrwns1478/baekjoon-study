import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

n = int(input())
arr = list()
for _ in range(n):
    r, c = map(int, input().split())
    arr.append((r,c))
dp = [[-1] * (n+1) for _ in range(n+1)]

def calc(s, e):
    result = float("inf")
    if dp[s][e] != -1: # 이미 계산한 구간일 때
        return dp[s][e]
    if s == e: # 1개 행렬일 때
        return 0
    if s+1 == e: # 2개 행렬일 때
        return arr[s-1][0] * arr[s-1][1] * arr[e-1][1]
    for i in range(s, e): # 3개 이상 행렬일 때
        a = arr[s-1][0] * arr[i-1][1] * arr[e-1][1]
        result = min(result, calc(s, i) + calc(i+1, e) + a) # 앞뒤 구간의 행렬을 합치기 위한 연산 횟수
    dp[s][e] = result
    return dp[s][e]

print(calc(1, n))