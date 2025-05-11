n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
res = 0
answer = n+1

while right < n:
    res += arr[right]
    while res >= s:
        answer = min(answer, right - left + 1)
        res -= arr[left]
        left += 1
    right += 1

print(answer * (answer < n+1))