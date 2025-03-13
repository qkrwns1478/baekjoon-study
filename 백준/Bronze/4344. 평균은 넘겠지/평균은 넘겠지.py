c = int(input())
for _ in range(c):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]
    cnt = 0
    for i in range(1, len(arr)):
        if arr[i] > avg:
            cnt += 1
    ans = (cnt / arr[0]) * 100
    print(f"{ans:.3f}%")