from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

Arr = []
indexes = [0] * n
visited = [-1] * n

for i in range(n):
    tmp = bisect_left(Arr, arr[i])
    if tmp == len(Arr):
        Arr.append(arr[i])
    else:
        Arr[tmp] = arr[i]
    indexes[tmp] = i
    if tmp > 0:
        visited[i] = indexes[tmp - 1]

print(len(Arr))

idx = indexes[len(Arr) - 1]
result = []
while idx != -1:
    result.append(arr[idx])
    idx = visited[idx]
    
result.reverse()
print(*result)