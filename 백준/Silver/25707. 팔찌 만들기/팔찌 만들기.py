import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = n // 2
ans = abs(arr[1] - arr[0])
for i in range(2, m+1):
    ans += abs(arr[i] - arr[i-1])
ans += abs(arr[m+1] - arr[0])
for i in range(m+2, n):
    ans += abs(arr[i] - arr[i-1])
ans += abs(arr[m] - arr[n-1])
print(ans)