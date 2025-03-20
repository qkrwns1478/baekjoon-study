import sys

def ran():
    start = 1
    end = max(arr)

    while start <= end:
        mid = (start + end) // 2 # 나누는 수
        tmp = sum(arr[i] // mid for i in range(n))
        if tmp >= k: # 나누는 값이 작은 경우 + 맞은 경우라도 끝이 아님!
            start = mid + 1
        else: # 나누는 값이 큰 경우
            end = mid - 1

    print(end) # end가 최대 길이
    return

n, k = map(int, sys.stdin.readline().split())
arr = list()
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

ran()