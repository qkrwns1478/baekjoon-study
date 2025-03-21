def getDivisor(n):
    answer = list()

    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            answer.append(i) 
            if (i**2) != n : 
                answer.append(n // i)

    answer.sort()
    return answer

while True:
    n = int(input())

    if n == -1:
        break
    
    dlist = getDivisor(n)
    
    if sum(dlist[:-1]) == n:
        print(n, "= ", end="")
        print(*dlist[:-1], sep=" + ")
    else:
        print(n, "is NOT perfect.")