import sys
input = sys.stdin.readline

def test(n):
    if n == 1:
        if arr[0] == 1:
            return 2
        else:
            return 1
    res = 1
    for i in range(n):
        if res >= arr[i]:
            res += arr[i]
        else:
            return res
    return res

n = int(input())
arr = list(map(int, input().strip().split()))
arr.sort()

print(test(n))