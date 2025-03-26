n, k = map(int, input().split())
arr = list()
for _ in range(n):
    coin = int(input())
    if coin <= k:
        arr.append(coin)
n = len(arr)

answer = 0
while k > 0:
    tmp = arr.pop()
    answer += k // tmp
    k -= (k // tmp) * tmp
print(answer)