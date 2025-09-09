def get_primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    res = [i for i, flag in enumerate(is_prime) if flag]
    return res

n = int(input())
cnt = 0
if n >= 2:
    arr = get_primes(n)
    l, r = 0, 0
    total = arr[0]
    while l <= r and r < len(arr):
        if total > n:
            total -= arr[l]
            l += 1
        elif total < n:
            r += 1
            if r >= len(arr):
                break
            total += arr[r]
        else:
            cnt += 1
            r += 1
            if r >= len(arr):
                break
            total += arr[r]
print(cnt)