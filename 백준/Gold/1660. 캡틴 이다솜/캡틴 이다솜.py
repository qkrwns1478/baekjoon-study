n = int(input())
def get_sum(i):
    return i * (i+1) // 2
arr = list()
num = 0
idx = 1
while True:
    num += get_sum(idx)
    if num > n:
        break
    arr.append(num)
    idx += 1

dp = [float("inf")] * (n+1)
for i in range(1, n+1):
    for j in arr:
        if i <= j:
            if i == j:
                dp[i] = 1
            break
        dp[i] = min(dp[i], dp[i-j] + 1)

print(dp[n])