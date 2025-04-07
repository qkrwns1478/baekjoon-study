import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
rev = arr[::-1]
dp1 = [1] * n
dp2 = [1] * n

for i in range(n):
    cnt1 = 0
    cnt2 = 0
    for j in range(i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)
        if rev[i] > rev[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
#print(dp1)
#print(dp2)
dp2.reverse()
    
result = [0] * n
for i in range(n):
    result[i] = dp1[i] + dp2[i] - 1
#print(result)
print(max(result))