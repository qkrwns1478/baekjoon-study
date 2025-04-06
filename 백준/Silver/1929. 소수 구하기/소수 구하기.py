import sys
input = sys.stdin.readline

def prime_nums(n):
    arr = [i for i in range(n+1)]
    end = int(n**0.5)
    for i in range(2, end+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
    return [i for i in arr[2:] if arr[i]]

m, n = map(int, input().split())
arr = prime_nums(n)
for i in arr:
    if i >= m:
        print(i)