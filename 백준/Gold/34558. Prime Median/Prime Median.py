from bisect import bisect_left, bisect_right
from sys import stdin
input = stdin.readline

max_b = 10**6
is_prime = [True] * (max_b+1)
is_prime[0], is_prime[1] = False, False
for i in range(2, int(max_b ** 0.5)+1):
    if is_prime[i]:
        for j in range(i*i, max_b+1, i):
            is_prime[j] = False

primes = [i for i in range(len(is_prime)) if is_prime[i]]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    s = bisect_left(primes, a)
    e = bisect_right(primes, b)
    cnt = e - s
    if cnt % 2:
        print(primes[s + cnt//2])
    else:
        print(-1)