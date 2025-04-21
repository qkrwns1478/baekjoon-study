n = int(input())
if n == 1:
    print("*")
else:
    print("*".rjust(n, ' '))
    for i in range(2, n+1):
        print(' ' * (n-i) + '* ' * i ,sep='')