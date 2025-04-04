from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

Arr = [float("inf")] * n

for i in range(n):
    tmp = bisect_left(Arr, arr[i])
    if tmp < n:
        Arr[tmp] = arr[i]

answer = 0
for i in Arr:
    if i < float("inf"):
        answer += 1
        
print(answer)