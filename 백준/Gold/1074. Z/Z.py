def r_map(n, r, k):
    if n == 0:
        return 0
    if r < 2**(n-1) + k:
        return r_map(n-1, r, k)
    else:
        return 4**n // 2 + r_map(n-1, r, k+ 2**(n-1))
def c_map(n, c, k):
    if n == 0:
        return 0
    if c < 2**(n-1) + k:
        return c_map(n-1, c, k)
    else:
        return 4**n // 4 + c_map(n-1, c, k+ 2**(n-1))

n, r, c = map(int, input().split())
answer = r_map(n, r, 0)
answer += c_map(n, c, 0)
print(answer)