import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s, e = 0, 0

for i in arr:
    if s < i:
        s = i
    e += i
    
while s <= e:
    mid = (s+e)//2
    sum = 0
    cnt = 0
    
    for i in range(n):
        if sum + arr[i] > mid:
            cnt += 1
            sum = 0
        sum += arr[i]
    if sum != 0:
        cnt += 1
    if cnt > m:
        s = mid + 1
    else:
        e = mid - 1
print(s)