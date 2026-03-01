import sys
input=sys.stdin.readline
N,M=map(int,input().split())
S=input().strip()
A=[(S[i],i) for i in range(N)]
A.sort(key=lambda x:(x[0],x[1]))
A=A[M:]
A.sort(key=lambda x:x[1])
for i in range(len(A)):
    print(A[i][0],end='')
