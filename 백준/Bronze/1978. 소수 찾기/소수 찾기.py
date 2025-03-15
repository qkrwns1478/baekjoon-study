def prime_numbers(n):
    arr = [i for i in range(n+1)]
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0: continue
        for j in range(i*i, n+1, i): arr[j] = 0
    return [i for i in arr[2:] if arr[i]]

n = int(input())
nums = list(map(int, input().split()))
prime = prime_numbers(max(nums))

answer = sum(1 for i in nums if i in prime)
print(answer)