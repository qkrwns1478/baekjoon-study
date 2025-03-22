import sys
input = sys.stdin.readline

n = int(input())
i = 0
answer = 0

while i < n:
    tmp = 0
    k = n-i
    while k > 0:
        tmp += k % 10
        k //= 10
    #print(tmp, n-i)
    if tmp + (n-i) == n:
        answer = n-i
    i += 1

print(answer)