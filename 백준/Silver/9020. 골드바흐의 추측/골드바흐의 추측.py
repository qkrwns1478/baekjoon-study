def is_prime(n):
    if(n == 1):
        return False
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

def gold(a, b):
    if(is_prime(a) and is_prime(b)):
        print(a, b)
        return
    else:
        gold(a-1, b+1)
        
t = int(input())
for _ in range(t):
    n = int(input())
    gold(n//2, n//2)
    