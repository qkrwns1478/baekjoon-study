import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

drr = {}
srr = list(set(arr))
srr.sort()
for i in range(len(srr)):
    drr[srr[i]] = i
#print(drr)

for i in range(n-1):
    print(drr[arr[i]], end=" ")
print(drr[arr[n-1]])