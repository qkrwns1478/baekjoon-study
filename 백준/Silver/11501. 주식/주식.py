from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_val = 0
    answer = 0
    for i in range(N-1, -1, -1):
        if arr[i] > max_val:
            max_val = arr[i]
        else:
            answer += max_val - arr[i]
    print(answer)
