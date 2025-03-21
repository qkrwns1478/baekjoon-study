import sys
input = sys.stdin.readline

def bubble_sort(arr, k):
    n = len(arr)
    cnt = 0
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt += 1
                if cnt == k:
                    return arr
    return -1

n, k = map(int,input().split())
arr = list(map(int, input().split()))
answer = bubble_sort(arr,k)
if answer != -1:
    print(*answer)
else:
    print(-1)