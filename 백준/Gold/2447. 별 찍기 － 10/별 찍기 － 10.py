import sys
input = sys.stdin.readline

n = int(input())
arr = [[" " for _ in range(n)] for _ in range(n)]

nn = n
k = 0
while nn > 1:
    nn //= 3
    k += 1
#print(k)

def divide(k, x, y):
    global arr
    
    if k == 1:
        arr[x][y] = "*"
        arr[x][y+1] = "*"
        arr[x][y+2] = "*"
        arr[x+1][y] = "*"
        arr[x+1][y+2] = "*"
        arr[x+2][y] = "*"
        arr[x+2][y+1] = "*"
        arr[x+2][y+2] = "*"
        return

    else:
        dn = 3**(k-1)
        divide(k-1, x, y)
        divide(k-1, x, y+dn)
        divide(k-1, x, y+dn*2)
        divide(k-1, x+dn, y)
        divide(k-1, x+dn, y+dn*2)
        divide(k-1, x+dn*2, y)
        divide(k-1, x+dn*2, y+dn)
        divide(k-1, x+dn*2, y+dn*2)

divide(k, 0, 0)
for i in range(n):
    print(*arr[i], sep="")