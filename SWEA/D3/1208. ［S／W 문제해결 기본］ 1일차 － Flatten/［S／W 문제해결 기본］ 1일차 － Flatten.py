for t in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    for _ in range(n):
        arr.sort()
        arr[0] += 1
        arr[-1] -= 1
    arr.sort()
    print(f"#{t} {arr[-1] - arr[0]}")