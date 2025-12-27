import sys
input = sys.stdin.readline
    
n, k = map(int, input().split())
arr = [0]
z = [True]

for i in range(1, n+1):
    bi = int(input(), 2)
    if z[i-1]: b = bi
    else: b = int(bin(bi)[2:].zfill(k)[::-1], 2)
    
    flag = False
    for j in range(i):
        a = arr[j]
        if a & b == b:
            flag = True
            break
    if flag:
        print("WellKnown")
    else:
        print("AdHoc")
    arr.append(b)
    z.append(flag)