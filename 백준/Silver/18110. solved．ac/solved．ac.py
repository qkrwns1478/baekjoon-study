from sys import stdin
input = stdin.readline

def round(n):
    if n - int(n) >= 0.5: return int(n)+1
    else: return int(n)

N = int(input())
if N == 0:
    print(0)
    exit()
M = round(N * 0.15)
A = list(int(input()) for _ in range(N))
A.sort()

if M > 0:
    print(round(sum(A[M:-M]) / (N-2*M)))
else:
    print(round(sum(A) / N))