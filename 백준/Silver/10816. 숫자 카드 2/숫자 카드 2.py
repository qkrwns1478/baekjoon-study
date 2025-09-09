import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

d = defaultdict(int)
for i in arr1:
    d[i] += 1

res = [0] * m
for i in range(m):
    if arr2[i] in d:
        res[i] += d[arr2[i]]
print(*res)