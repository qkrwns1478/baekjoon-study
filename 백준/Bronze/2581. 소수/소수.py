def sieve(m, n):
    arr = [True] * (n+1)
    arr[0] = arr[1] = False
    end = int(n**0.5)
    
    for i in range(2, end + 1):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = False
                
    return [i for i in range(m, n+1) if arr[i]]

m = int(input())
n = int(input())
answer = sieve(m, n)

if answer:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)