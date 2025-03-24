t = int(input())
for _ in range(t):
    answer = -1
    n = int(input())
    while n <= 10**18:
        x = 0
        for i in str(n):
            x += int(i)
        #print("x =", x)
        
        if x % 2 == 1:
            answer = n
            break
        else:
            n += n
    print(answer)