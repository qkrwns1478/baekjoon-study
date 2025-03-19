def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    answer = [0, 1]
    for i in range(2, n+1):
        answer[0], answer[1] = answer[1], answer[0]+answer[1]
    return answer[1]

n = int(input())
print(fibo(n))