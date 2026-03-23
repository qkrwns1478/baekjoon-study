from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
arr = [list() for _ in range(200001)]

for i in range(N):
    idx = 1
    while idx ** 2 <= A[i]:
        if idx ** 2 == A[i]:
            arr[idx].append(i+1)
        elif A[i] % idx == 0:
            arr[idx].append(i+1)
            arr[A[i] // idx].append(i+1)
        idx += 1
    idx = A[i] * 2
    while idx < 200001:
        arr[idx].append(i+1)
        idx += A[i]

for i in range(len(arr)):
    arr[i].sort()

for _ in range(Q):
    li, ri, di = map(int, input().split())
    right = bisect_right(arr[di], ri)
    left = bisect_left(arr[di], li)
    print(right - left, end=' ')
