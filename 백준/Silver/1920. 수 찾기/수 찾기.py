def bin_search(arr, key, pl, pr):
    if pl > pr:
        return 0

    center = (pl + pr) // 2
    if arr[center] == key:
        return 1
    elif arr[center] < key:
        return bin_search(arr, key, center+1, pr)
    else:
        return bin_search(arr, key, pl, center-1)

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int, input().split()))

for num in arr2:
    print(bin_search(arr1, num, 0, n-1))