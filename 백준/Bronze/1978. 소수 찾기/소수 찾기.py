import sys
def is_prime(n):
    if(n == 1):
        return False
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in arr:
    if(is_prime(i)):
        cnt += 1
print(cnt)