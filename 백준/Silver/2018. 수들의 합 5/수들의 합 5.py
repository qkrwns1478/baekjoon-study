n = int(input())
l, r = 1, 1
ans = 0
sum = 0
while l <= n:
    if sum == n:
        ans += 1
        sum -= l
        l += 1
    elif sum < n:
        if r > n:
            break
        sum += r
        r += 1
    else:
        sum -= l
        l += 1
print(ans)