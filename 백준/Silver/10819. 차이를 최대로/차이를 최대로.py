import random

def cal(arr):
    answer = 0
    for i in range(n-1):
        answer += abs(arr[i] - arr[i+1])
    return answer

n = int(input())
arr = list(map(int, input().split()))
max_val = cal(arr)

for _ in range(10000):
    random.shuffle(arr)
    max_val = max(max_val, cal(arr))

print(max_val)