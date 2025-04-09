t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    for i in range(n // 3 + 1):
        answer += (n - 3*i) // 2 + 1
    print(answer)