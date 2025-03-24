import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

pl, pr = 0, n-1
answer = float("inf")
A, B = None, None

while pl < pr:
    a, b = arr[pl], arr[pr]
    #print(a, b, abs(a+b))
    if answer > abs(a+b):
        answer = abs(a+b)
        A, B = a, b
    elif abs(a) > abs(b):
        pl += 1
    else:
        pr -= 1

if A > B: A, B = B, A
print(A, B)