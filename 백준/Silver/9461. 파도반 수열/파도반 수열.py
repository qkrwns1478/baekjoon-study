import sys
input = sys.stdin.readline

t = int(input())
memo = dict()
for _ in range(t):
    n = int(input())
    
    def pado(n):
        if n in memo:
            return memo[n]
        if n <= 3:
            return 1
        else:
            memo[n] =  pado(n-3) + pado(n-2)
            return memo[n]

    print(pado(n))